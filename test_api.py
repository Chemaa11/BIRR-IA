from gemini_api import generar_respuesta

print("================================")
print("       BIRR-IA ASISTENTE")
print("================================")

pregunta = input("\nEscribe tu pregunta: ")

respuesta = generar_respuesta(pregunta)

print("\n--- RESPUESTA DE BIRR-IA ---\n")
print(respuesta)