import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Cargar las variables de entorno
load_dotenv()

# Obtener la clave API
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró la clave API en el archivo .env")

# Inicializar el cliente de Gemini
client = genai.Client(api_key=API_KEY)

# Modelos disponibles
MODELOS = [
    "gemini-3.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.7-flash",
    "gemini-3.8-flash"
]


# Función para generar contenido con Gemini
def generar_respuesta(prompt):

    for modelo in MODELOS:

        try:
            respuesta = client.models.generate_content(
                model=modelo,
                contents=prompt
            )

            return respuesta.text

        except errors.APIError as e:

            print(f"Error en {modelo}: {e.code}")

            if e.code not in (404, 503):
                raise

    raise RuntimeError(
        "No fue posible obtener una respuesta de Gemini."
    )