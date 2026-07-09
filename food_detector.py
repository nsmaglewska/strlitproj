from transformers import (
    CLIPProcessor,
    CLIPModel
)
from PIL import Image
import torch
import streamlit as st
MODEL_NAME = "openai/clip-vit-base-patch32"
@st.cache_resource
def load_clip():
    model = CLIPModel.from_pretrained(
        MODEL_NAME
    )
    processor = CLIPProcessor.from_pretrained(
        MODEL_NAME
    )
    return model, processor
model, processor = load_clip()
FOOD_CLASSES = [
    "banana",
    "apple",
    "orange",
    "pizza",
    "hamburger",
    "rice",
    "pasta",
    "chicken",
    "fish",
    "egg",
    "milk",
    "bread",
    "cheese",
    "tomato",
    "potato"
]
def detect_food(image_file):

    image = Image.open(
        image_file
    )
    labels = [
        f"a photo of {x}"
        for x in FOOD_CLASSES
    ]
    inputs = processor(
        text=labels,
        images=image,
        return_tensors="pt",
        padding=True
    )
    with torch.no_grad():

        output = model(
            **inputs
        )
    probs = output.logits_per_image.softmax(
        dim=1
    )
    index = probs.argmax().item()
    return {
        "food": FOOD_CLASSES[index],
        "confidence": probs[0][index].item()
    }
