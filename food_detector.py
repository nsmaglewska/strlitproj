import base64
from openai import OpenAI
import streamlit as st
client = OpenAI(
    api_key=st.secrets["API_KEY"],
    base_url=st.secrets["BASE_URL"]
)
MODEL = "gemini-2.5-flash"

def detect_food(image_file):
    image_bytes = image_file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Jesteś systemem rozpoznającym żywność. "
                    "Odpowiadaj wyłącznie nazwą produktu spożywczego "
                    "bez dodatkowych wyjaśnień."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Jaki produkt spożywczy znajduje się na zdjęciu?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content.strip()
