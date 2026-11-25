from pathlib import Path
from analizador import AnalizadorPDF

# Crear el analizador
analizador = AnalizadorPDF()

print("====================================")
print("    BIRR-IA ANALIZADOR INTELIGENTE")
print("====================================")

# Ubicación del documento
ruta = (
    Path(__file__).resolve().parent
    / "documentos"
    / "investigacion.pdf"
)

try:

    print("\nLeyendo documento PDF...")

    analizador.leer_pdf(ruta)

    informacion = analizador.obtener_informacion()

    print("\n--- INFORMACIÓN DEL DOCUMENTO ---")

    print(f"Páginas: {informacion['paginas']}")
    print(f"Palabras: {informacion['palabras']}")
    print(f"Caracteres: {informacion['caracteres']}")

    print("\nAnalizando documento con Google Gemini...")
    print("Por favor, espera unos momentos.")

    resultado = analizador.analizar()

    print("\n--- RESULTADO DEL ANÁLISIS ---\n")
    print(resultado)

    print("\nPuedes realizar preguntas sobre el documento.")
    print("Escribe 'salir' para finalizar.")

    while True:

        pregunta = input("\nTu pregunta: ").strip()

        if pregunta.lower() == "salir":
            print("\nAnálisis finalizado.")
            break

        if not pregunta:
            continue

        try:
            respuesta = analizador.preguntar(pregunta)

            print(f"\nBIRR-IA: {respuesta}")

        except Exception as error:
            print(f"\nError al responder: {error}")

except FileNotFoundError:

    print("\nERROR: No se encontró el archivo PDF.")
    print("Verifica que exista:")
    print(ruta)

except Exception as error:

    print(f"\nOcurrió un error: {error}")