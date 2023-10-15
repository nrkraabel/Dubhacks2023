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


def detect_faces(img, img_path=None):
    data = []
    client = vision.ImageAnnotatorClient()
    _, encoded_image = cv2.imencode('.jpg', img)
    image = vision.Image(content=encoded_image.tobytes())
    faces = client.face_detection(image=image).face_annotations
    if img_path and isinstance(img_path, str):
        print("img_path in detect_faces:", img_path)
        lat, lon = extract_lat_long(img_path)
    else:
        lat, lon = None, None
    model = modelLoad()
    videoID = 0
    for face in faces:
        X = [vertex.x for vertex in face.bounding_poly.vertices]
        Y = [vertex.y for vertex in face.bounding_poly.vertices]
        face_image = img[min(Y): max(Y), min(X): max(X)]
        
        # Enhance the face image using super-resolution
        # enhanced_face = super_resolve(face_image)
        
        file_name = str(uuid.uuid4()) + '.jpg'
        
        # Save the enhanced face instead of the original low-res face
        cv2.imwrite(file_name, face_image)
        

        if not lat and not lon:  # If image path is available but no geolocation data
            lat, lon = predict_Geo(file_name)

        embedding = get_embedding(file_name, model)
        data.append([file_name, videoID, str(embedding.tolist()), 0, lat or 0, lon or 0])
        videoID += 1
        os.remove(file_name)
    return data

def DataUpload(data):
    if not data:
        return
    db = SQLAccess()
    query = "insert into FaceEmbeddingEntryTable ([UploadId],[VideoId], [Embedding], [Bluriness], [Longitude], [Latitude]) values (?,?,?,?,?,?)"
    db.execute_non_query_many(query, data)

def video_imgSplit(file_name, content_type, uploadID):
    if content_type == "picture":
        return detect_faces(cv2.imread(file_name), uploadID, file_name)
    cap = cv2.VideoCapture(file_name)
    frames_to_check = int(math.ceil(cap.get(cv2.CAP_PROP_FPS)) / 2)
    data = []
    best_frame, best_laplacian = [], 0
    while True:
        ret, frame = cap.read()
        if frame is None:
            facedata = detect_faces(best_frame, uploadID)
            if facedata:
                data.extend(facedata)
            break
        laplacian = cv2.Laplacian(frame, cv2.CV_64F).var()
        
        if len(best_frame) == 0 or laplacian > best_laplacian:
            best_frame, best_laplacian = frame, laplacian
        if cap.get(1) % frames_to_check == 0:
            facedata = detect_faces(best_frame, uploadID)
            if facedata:
                data.extend(facedata)
            best_frame, best_laplacian = [], 0
    return data

def modelLoad():
    model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
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
    
def super_resolve(img):
    # Ensure you're using GPU if available
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # # Load a pre-trained EDSR model
    # model = models.edsr(scale_factor=4, pretrained=True).eval().to(device)

     # Convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Normalize the image
    img_rgb = img_rgb.astype(np.float32) / 255.0
    
    # Convert to tensor
    img_tensor = torch.tensor(img_rgb).permute(2, 0, 1).unsqueeze(0).to(device)
    
    # Apply the super-resolution model
    with torch.no_grad():
        output = model(img_tensor)
        
    # Convert tensor to numpy image
    output_img = output.squeeze().permute(1, 2, 0).cpu().numpy()
    output_img = (output_img.clip(0, 1) * 255).astype(np.uint8)
    
    # Convert RGB back to BGR
    output_bgr = cv2.cvtColor(output_img, cv2.COLOR_RGB2BGR)
    
    return output_bgr



