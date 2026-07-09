from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch


MODEL_NAME = "openai/clip-vit-base-patch32"


model = CLIPModel.from_pretrained(
    MODEL_NAME
)

processor = CLIPProcessor.from_pretrained(
    MODEL_NAME
)


# Lista produktów, które chcemy rozpoznawać
FOOD_CLASSES = [
    "apple",
    "banana",
    "orange",
    "pizza",
    "hamburger",
    "pasta",
    "rice",
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

    image = Image.open(image_file)

    texts = [
        f"a photo of {food}"
        for food in FOOD_CLASSES
    ]


    inputs = processor(
        text=texts,
        images=image,
        return_tensors="pt",
        padding=True
    )


    with torch.no_grad():

        outputs = model(**inputs)


    logits = outputs.logits_per_image

    probabilities = logits.softmax(
        dim=1
    )


    best_index = probabilities.argmax().item()


    food = FOOD_CLASSES[best_index]

    confidence = probabilities[0][best_index].item()


    return {
        "food": food,
        "confidence": confidence
    }
