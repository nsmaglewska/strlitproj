from langchain_core.prompts import ChatPromptTemplate

template = """
Jesteś dietetykiem.
Przeanalizuj produkt:
{context}
Podaj:
- ocenę zdrowotności 1-10
- zalety
- wady
- dla kogo produkt jest dobry
- czy pasuje do redukcji
- krótkie zalecenie
"""
def analyze_nutrition(
        context,
        model
):
    prompt = ChatPromptTemplate.from_template(
        template
    )
    chain = prompt | model
    return chain.invoke(
        {
            "context": context
        }
    )
