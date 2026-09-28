from google import genai
from PIL import Image

client = genai.Client(
    api_key="AQ.Ab8RN6IMUOV2OMUkhYXZtNsXgFOsDXx-CRlzrE1MrdWRbbBOxQ"
)

imagen = Image.open("foto.jpg")

respuesta = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        "Describe detalladamente esta imagen",
        imagen
    ]
)

print(respuesta.text)