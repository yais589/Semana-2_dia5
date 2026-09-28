from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6IMUOV2OMUkhYXZtNsXgFOsDXx-CRlzrE1MrdWRbbBOxQ"
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Hola Gemini, dime qué es Python."
)

print(response.text)