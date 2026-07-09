from langchain_core.prompts import ChatPromptTemplate

PROMPT = """
Jesteś dietetykiem.

Przeanalizuj produkt:

{context}

Podaj:

1. Ocena zdrowotności 1-10
2. Najważniejsze zalety
3. Możliwe wady
4. Czy produkt pasuje do zdrowej diety
5. Krótkie zalecenie
"""
def analyze_nutrition(
        context,
        model
):
    prompt = ChatPromptTemplate.from_template(
        PROMPT
    )
    chain = prompt | model
    return chain.invoke(
        {
            "context": context
        }
    )
