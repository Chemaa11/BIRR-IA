import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Cargar la clave API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No se encontró la clave API en el archivo .env")

# Conectar con Google Gemini
client = genai.Client(api_key=api_key)

# Modelos alternativos
modelos = [
    "gemini-3.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.7-flash",
    "gemini-3.8-flash"
]

# Pregunta de prueba
pregunta = "Hola, preséntate y explica cómo puedes ayudar a un estudiante universitario."

# Probar los modelos disponibles
for modelo in modelos:
    print(f"\nProbando modelo: {modelo}")

    try:
        response = client.models.generate_content(
            model=modelo,
            contents=pregunta
        )

        print("\n--- CONEXIÓN EXITOSA ---")
        print(f"Modelo utilizado: {modelo}")
        print("\n--- RESPUESTA DE GEMINI ---\n")
        print(response.text)
        break

    except errors.APIError as e:
        print(f"Error con {modelo}: {e.code}")

        if e.code not in (404, 503):
            print("Se requiere revisar el error:", e)
            break

        print("Probando otro modelo...")

else:
    print("\nNo fue posible conectar con los modelos seleccionados.")