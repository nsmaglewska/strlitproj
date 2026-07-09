import streamlit as st
from openai import OpenAI
import os
import fitz
from food_detector import detect_food
from nutrition_rag import retrieve_food_context
from nutrition_analyzer import analyze_nutrition
from custom_model_chat import get_model
from openai import RateLimitError

model = get_model()

# a

st.set_page_config(layout="wide", page_title="Food nutrition app")
st.title("Food nutrition app")

# api_key, base_url = os.environ["API_KEY"], os.environ["BASE_URL"]
api_key, base_url = st.secrets["API_KEY"], st.secrets["BASE_URL"]
selected_model = "gemini-2.5-flash"

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "W czym mogę pomóc?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not api_key:
        st.info("Invalid API key.")
        st.stop()
    client = OpenAI(api_key=api_key, base_url=base_url)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model = selected_model,
        messages = st.session_state.messages)

    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

uploaded_image = st.file_uploader(
    "Dodaj zdjęcie jedzenia",
    type=["jpg", "jpeg", "png"],
    key="food_image"
)
if uploaded_image:
    st.image(
        uploaded_image,
        width=300
    )
    if "food_name" not in st.session_state:
        result = detect_food(
            uploaded_image
        )
        st.session_state.food_name = result["food"]
        st.session_state.confidence = result["confidence"]
    food_name = st.session_state.food_name
    st.success(
        f"Rozpoznano: {food_name}"
    )
    st.write(
        f"Pewność: {st.session_state.confidence:.2f}"
    )
    context = retrieve_food_context(
        food_name
    )
    if context:
        try:
        answer = analyze_nutrition(
            context,
            model
        )
        st.subheader(
            "Analiza wartości odżywczych"
        )
        st.write(
            answer.content
        )
    except RateLimitError:
        st.error(
            "Przekroczono limit Gemini API. "
            "Spróbuj później lub zmień model."
        )
    else:
        st.warning(
            "Nie znaleziono produktu w bazie."
        )
