import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from torch.utils.data import DataLoader
from PIL import Image
import os

def Create_Geo():
    # Path to the 'GeoLocation' folder
    folder_path = "./GeoData"

    # Retrieve all jpeg files from the folder
    all_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

    # Extract latitude and longitude from filename and store in the desired format
    data = []
    for file in all_files:
        # Removing '.jpeg' and splitting by ','
        lat_str, lng_str = file[:-5].split(',')
        lat, lng = float(lat_str), float(lng_str)
        data.append((os.path.join(folder_path, file), (lat, lng)))


    # Now 'data' contains the desired format: [('path_to_image.jpg', (lat, lng)), ...]
    print(data)
    return data


# Define Transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Dataset
class GeoDataset(torch.utils.data.Dataset):
    def __init__(self, data, transform=None):
        self.data = data
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path, coords = self.data[idx]
        img = Image.open(img_path).convert("RGB")
        if self.transform:
            img = self.transform(img)
        return img, torch.tensor(coords)
    
def train_geo():    
    data = Create_Geo()

    dataset = GeoDataset(data, transform)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    # Model
    model = resnet50(pretrained=True)
    model.fc = torch.nn.Linear(model.fc.in_features, 2)  # Latitude and Longitude
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    criterion = torch.nn.MSELoss()  # Mean Squared Error Loss

    epochs = 50
    # Training Loop
    model.train()
    for epoch in range(epochs):
        for imgs, coords in dataloader:
            outputs = model(imgs)
            loss = criterion(outputs, coords)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item()}")

def predict_Geo(img_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    model = resnet50(pretrained=True)
    model.fc = torch.nn.Linear(model.fc.in_features, 2)  # Latitude and Longitude
    model_path = "GeoLocationModel.pt"
    model.load_state_dict(torch.load(model_path))
    model.eval()

    img = Image.open(img_path).convert("RGB")
    img = transform(img).unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        output = model(img)
    lat, lon = output[0][0].item(), output[0][1].item()

    return lat, lon

