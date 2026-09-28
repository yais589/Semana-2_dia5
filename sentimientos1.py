from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6IMUOV2OMUkhYXZtNsXgFOsDXx-CRlzrE1MrdWRbbBOxQ"
)

textos = [
    "Me encanta este producto",
    "Este servicio es horrible",
    "Hoy es un día normal",
    "Estoy muy feliz con los resultados",
    "No recomiendo esta empresa",
    "I love this movie",
    "This game is terrible",
    "The weather is okay",
    "I am very excited",
    "I feel disappointed"
]

for texto in textos:

    prompt = f"""
Analiza este texto:

{texto}

Devuelve:
- Sentimiento
- Entidades detectadas
"""

    respuesta = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    print("\n" + "=" * 60)
    print(texto)
    print(respuesta.text)