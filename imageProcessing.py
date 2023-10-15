import json
import math
import uuid
from google.cloud import vision
import cv2
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from torchvision.models.resnet import ResNet50_Weights
from PIL import Image

from SQLAccess import SQLAccess

import os

content_type = "video"
file_name = "vid.mov"


def detect_faces(img, uploadID):
    data = []
    client = vision.ImageAnnotatorClient()
    success, encoded_image = cv2.imencode('.jpg', img)
    content = encoded_image.tobytes()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = (
        "UNKNOWN",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    )

    model = modelLoad()
    videoID = 0
    for face in faces:
        #print(f"anger: {likelihood_name[face.anger_likelihood]}")
        #print(f"joy: {likelihood_name[face.joy_likelihood]}")
        #print(f"surprise: {likelihood_name[face.surprise_likelihood]}")


        X = [vertex.x for vertex in face.bounding_poly.vertices]
        Y = [vertex.y for vertex in face.bounding_poly.vertices]

        Xmax = max(X)
        Xmin = min(X)

        Ymax = max(Y)
        Ymin = min(Y)


        #cv2.rectangle(img, (Xmin, Ymin), (Xmax, Ymax), (0, 0, 255), 2)

        faces = img[Ymin: Ymax, Xmin: Xmax]
        file_name = str(uuid.uuid4()) + '.jpg'
        cv2.imwrite(file_name, faces)
        embedding = get_embedding(file_name, model)
        data.append([uploadID,videoID,str(embedding.tolist()), 0,0,0])
        videoID+=1
        os.remove(file_name)
    return data

def DataUpload(data):
    if len(data) == 0:
        return
    db = SQLAccess()
    query = """
    insert into FaceEmbeddingEntryTable ([UploadId],[VideoId], [Embedding], [Bluriness], [Longitude], [Latitude]) values 
    (?,?,?,?,?,?)
    """
    db.execute_non_query_many(query, data)


def video_imgSplit(file_name, content_type, uploadID):
    if content_type == "picture":
        img = cv2.imread(file_name)
        return detect_faces(img,uploadID)
        
    elif content_type == "video":
        cap = cv2.VideoCapture(file_name)
        fps = math.ceil(cap.get(cv2.CAP_PROP_FPS))

        frames_to_check = int(fps/2)

        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))

        frame_num = 1

        best_frame = []
        best_laplacian = 0

        total_pics_num = 1
        data = []
        while (True):
            ret, frame = cap.read()

            if frame is None:
                data.append(detect_faces(best_frame, uploadID))
                #cv2.imwrite(file_name.split('.')[0] + "_img_" + str(total_pics_num) + ".jpg", best_frame)
                break

            font = cv2.FONT_HERSHEY_SIMPLEX

            laplacian = cv2.Laplacian(frame, cv2.CV_64F).var()

            if len(best_frame) == 0 or laplacian > best_laplacian:
                best_frame = frame
                best_laplacian = laplacian


            if frame_num % frames_to_check == 0:
                data.append(detect_faces(best_frame, uploadID))
                #cv2.imwrite(file_name.split('.')[0] + "_img_" + str(total_pics_num) + ".jpg", best_frame)
                best_frame = []
                best_laplacian = 0

                total_pics_num += 1

            frame_num += 1
    return data
def modelLoad():
    # Load a pre-trained resnet model using the recommended weight enum
    model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
    model.eval()

    # Remove the final layer to use the model as a feature extractor
    model = torch.nn.Sequential(*(list(model.children())[:-1]))

    return model


def get_embedding(img_path, model):
    preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    """Get embedding for a given image."""
    image = Image.open(img_path).convert("RGB")  # Convert image to RGB
    img_tensor = preprocess(image)
    img_tensor = img_tensor.unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        embedding = model(img_tensor)
    return embedding.squeeze()

def similarity(embedding1, embedding2):
    """Compute cosine similarity between two embeddings."""
    cos = torch.nn.CosineSimilarity(dim=0)
    return cos(embedding1, embedding2)

def image_difference_detection(imagefile, imagefile2, model):
    
    # Load and get embeddings for the two images
    embedding1 = get_embedding(imagefile,model)
    embedding2 = get_embedding(imagefile2, model)
    # print(embedding1.shape)
    torch.set_printoptions(threshold=10_000)
    tensor_str = str(embedding2)
    print(len(tensor_str))

    # Write to a txt file
    with open('tensor_output.txt', 'w') as f:
        f.write(tensor_str)
    # Compute similarity
    sim = similarity(embedding1, embedding2)

    return sim

def split_embedding(embedding_str, chunk_size=4000):
    """
    Splits a long embedding string into chunks of size chunk_size.
    Returns a list of chunks.
    """
    return [embedding_str[i:i+chunk_size] for i in range(0, len(embedding_str), chunk_size)]

def pull_data():
    batch_size = 100
    db = SQLAccess()

    # Get the total number of entries
    total_entries = len(db.execute_non_query_select("SELECT EntryId FROM FaceEmbeddingEntryTable"))
    
    batches = (total_entries + batch_size - 1) // batch_size  # Calculate number of batches
    all_data = []
    for batch_num in range(batches):
        offset = batch_num * batch_size
        query = f"SELECT * FROM FaceEmbeddingEntryTable ORDER BY EntryId OFFSET {offset} ROWS FETCH NEXT {batch_size} ROWS ONLY"
        batch_data = db.execute_non_query_select(query)

        # Process batch_data as required or yield it if you want to create a generator
        # For now, we'll just print the first row of each batch
        print(batch_data[0] if batch_data else "No Data")
        all_data.append(batch_data)

    # If you don't want to process the data here, you can return the data
    # return all_data
    return all_data


# def compareFaceUpload(file_name):
#     data = detect_faces(file_name, 1)
#     comparison 

DataUpload(video_imgSplit(file_name, content_type, 1))




# model = modelLoad()
# db = SQLAccess()
# data = []
# torch.set_printoptions(threshold=20_000)
# for i in range(2000):
#     query = """
#     insert into FaceEmbeddingEntryTable ([UploadId],[VideoId], [Embedding], [Bluriness], [Longitude], [Latitude]) values 
#     (?,?,?,?,?,?)
#     """
#     embedding = get_embedding("0000005.jpg",model)
#     # chunks = split_embedding(str(embedding))
#     data.append(["0",i,str(embedding), 0,0,0])
# db.execute_non_query_many(query, data)
