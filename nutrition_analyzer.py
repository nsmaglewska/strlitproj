from langchain_core.prompts import ChatPromptTemplate
from custom_model_chat import CustomChatModel

model = CustomChatModel(
    model="gemini-2.5-flash"
)

template = """
Jesteś dietetykiem.

Przeanalizuj poniższy produkt spożywczy.

{context}

Odpowiedz na pytania:

1. Czy produkt jest zdrowy?
2. Jakie są jego zalety?
3. Jakie są jego wady?
4. Dla kogo jest polecany?
5. Czy nadaje się na redukcję masy ciała?
6. Oceń produkt w skali 1-10 i uzasadnij ocenę.

Odpowiedź:
"""

def analyze_nutrition(context, model):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        "context": context
    })
    return response
