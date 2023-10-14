import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
def modelLoad():
    # Load a pre-trained resnet model (you can use other architectures like densenet or vgg)
    model = models.resnet50(pretrained=True)
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

    # Compute similarity
    sim = similarity(embedding1, embedding2)

    return sim

model = modelLoad()

print(image_difference_detection("0000005.jpg","0014_0002593_script.jpg", model))