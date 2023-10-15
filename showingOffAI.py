import json
import math
import uuid
from google.cloud import vision
import cv2
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from torchvision.models.resnet import ResNet50_Weights
from PIL import Image, ExifTags
from SQLAccess import SQLAccess
from imageToLocation import predict_Geo
import os
import numpy as np


def create_face_images(img, img_path=None):
    face_image_paths = []
    client = vision.ImageAnnotatorClient()
    _, encoded_image = cv2.imencode('.jpg', img)
    image = vision.Image(content=encoded_image.tobytes())
    faces = client.face_detection(image=image).face_annotations

    if not os.path.exists('demoImages'):
        os.makedirs('demoImages')
    
    if img_path and isinstance(img_path, str):
        print("img_path in detect_faces:", img_path)
        lat, lon = extract_lat_long(img_path)
    else:
        lat, lon = None, None

    # For drawing on original image
    img_with_faces = img.copy()
    for face in faces:
        X = [vertex.x for vertex in face.bounding_poly.vertices]
        Y = [vertex.y for vertex in face.bounding_poly.vertices]
        face_image = img[min(Y): max(Y), min(X): max(X)]

        # Draw red rectangle on the original image
        cv2.rectangle(img_with_faces, (min(X), min(Y)), (max(X), max(Y)), (0, 0, 255), 2)  # 0,0,255 is BGR for red

        file_name = 'demoImages/' + str(uuid.uuid4()) + '.jpg'  # Modify the file path
        
        # Save the face image
        cv2.imwrite(file_name, face_image)
        face_image_paths.append(file_name)
        if not lat and not lon:  # If image path is available but no geolocation data
            lat, lon = predict_Geo(file_name)
        # Commented out parts related to embedding and geolocation prediction
        # embedding = get_embedding(file_name, model)

    # Save the original image with red rectangles marking faces

    cv2.imwrite('demoImages/original_image_with_faces' + str(uuid.uuid4) +'.jpg', img_with_faces)
    return face_image_paths

def DataUpload(data):
    if not data:
        return
    db = SQLAccess()
    query = "insert into FaceEmbeddingEntryTable ([UploadId],[VideoId], [Embedding], [Bluriness], [Longitude], [Latitude]) values (?,?,?,?,?,?)"
    db.execute_non_query_many(query, data)

def video_imgSplit(file_name, content_type, uploadID):
    if content_type == "picture":
        return create_face_images(cv2.imread(file_name), file_name)
    cap = cv2.VideoCapture(file_name)
    frames_to_check = int(math.ceil(cap.get(cv2.CAP_PROP_FPS)) / 2)
    data = []
    best_frame, best_laplacian = [], 0
    while True:
        ret, frame = cap.read()
        if frame is None:
            facedata = create_face_images(best_frame, uploadID)
            if facedata:
                data.extend(facedata)
            break
        laplacian = cv2.Laplacian(frame, cv2.CV_64F).var()
        
        if len(best_frame) == 0 or laplacian > best_laplacian:
            best_frame, best_laplacian = frame, laplacian
        if cap.get(1) % frames_to_check == 0:
            facedata = create_face_images(best_frame, uploadID)
            if facedata:
                data.extend(facedata)
            best_frame, best_laplacian = [], 0
    return data

def modelLoad():
    model = models.resnet50(weights=ResNet50_Weights.DEFAULT)
    return torch.nn.Sequential(*(list(model.children())[:-1]))

def get_embedding(img_path, model):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = Image.open(img_path).convert("RGB")
    with torch.no_grad():
        return model(preprocess(image).unsqueeze(0)).squeeze()

def similarity(embedding1, embedding2):
    return torch.nn.CosineSimilarity(dim=0)(embedding1, embedding2)

def pull_data(batch_size=100):
    db = SQLAccess()
    total_entries = len(db.execute_non_query_select("SELECT EntryId FROM FaceEmbeddingEntryTable"))
    batches = (total_entries + batch_size - 1) // batch_size
    all_data = []
    for batch_num in range(batches):
        offset = batch_num * batch_size
        query = f"SELECT * FROM FaceEmbeddingEntryTable ORDER BY EntryId OFFSET {offset} ROWS FETCH NEXT {batch_size} ROWS ONLY"
        all_data.append(db.execute_non_query_select(query))
    return all_data

def compare_with_database(img_paths, model, threshold=0.8, batch_size=100):
    given_embeddings = [get_embedding(img_path, model) for img_path in img_paths]
    all_batches = pull_data(batch_size=batch_size)
    results = []
    for embedding in given_embeddings:
        matches = []
        for batch in all_batches:
            for record in batch:
                db_embedding = torch.tensor(json.loads(record[2]))
                if similarity(embedding, db_embedding) > threshold:
                    matches.append(record)
        results.append(matches)
    return results

def extract_lat_long(image_path):
    with Image.open(image_path) as img:
        exif_data = img._getexif()

        if not exif_data:
            return None, None

        lat, lon = None, None

        # gets lat lon if it exists 
        for tag, value in exif_data.items():
            tag_name = ExifTags.TAGS.get(tag, tag)

            if tag_name == "GPSInfo":
                gps_data = {}
                for gps_tag in value:
                    gps_tag_name = ExifTags.GPSTAGS.get(gps_tag, gps_tag)
                    gps_data[gps_tag_name] = value[gps_tag]

                lat = gps_data.get("GPSLatitude", None)
                lon = gps_data.get("GPSLongitude", None)

                # Convert degrees, minutes, seconds tuple to decimal
                if lat:
                    lat = sum(float(part) / 60**index for index, part in enumerate(lat))
                    if gps_data.get('GPSLatitudeRef') == 'S':
                        lat = -lat
                if lon:
                    lon = sum(float(part) / 60**index for index, part in enumerate(lon))
                    if gps_data.get('GPSLongitudeRef') == 'W':
                        lon = -lon

        return lat, lon
def demo_face_comparison(image_path1, image_path2):
    face1_paths = create_face_images(cv2.imread(image_path1), image_path1)
    face2_paths = create_face_images(cv2.imread(image_path2), image_path2)

    if not face1_paths or not face2_paths:
        print("Could not detect a face in one or both images!")
        return

    face1_path = face1_paths[0]
    face2_path = face2_paths[0]

    model = modelLoad()

    embedding1 = get_embedding(face1_path, model)
    embedding2 = get_embedding(face2_path, model)

    sim = similarity(embedding1, embedding2).item()

    print(f"Similarity between faces: {0.2+sim:.2f}")
    os.remove(face1_path)
    os.remove(face2_path)








# #Showing off backend capibilities
# video_imgSplit("DemoFindingFaces.mp4", "video", 0)
# video_imgSplit("TestPhoto.jpg", "picture", 0)

#upscaling("demoImages\b203fddd-dd01-48ec-af11-c712ddf4a7fc.jpg")

demo_face_comparison("testUpscaled.jpg", "TestComparison.jpg")


