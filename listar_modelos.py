import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No se encontró la clave API")

client = genai.Client(api_key=api_key)

print("\n--- MODELOS DISPONIBLES ---\n")

for modelo in client.models.list():
    if "generateContent" in (modelo.supported_actions or []):
        print(modelo.name)