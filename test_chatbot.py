from chatbot import Chatbot

# Crear nuestro chatbot
bot = Chatbot()

print("====================================")
print("       BIRR-IA CHAT INTELIGENTE")
print("====================================")

# Solicitar información del usuario
nombre = input("\n¿Cuál es tu nombre? ")
carrera = input("¿Qué carrera estudias? ")
objetivo = input("¿Cuál es tu objetivo académico? ")

# Configurar el perfil
bot.configurar_perfil(
    nombre,
    carrera,
    objetivo
)

print(f"\n¡Bienvenido, {nombre}!")
print("Soy BIRR-IA, tu asistente inteligente.")
print("Escribe 'salir' para terminar.")
print("Escribe 'limpiar' para borrar el historial.")

# Iniciar conversación
while True:

    mensaje = input("\nTú: ").strip()

    if not mensaje:
        continue

    if mensaje.lower() == "salir":
        print(f"\n¡Hasta pronto, {nombre}!")
        break

    if mensaje.lower() == "limpiar":
        bot.limpiar_historial()
        print("\nHistorial eliminado correctamente.")
        continue

    try:

        respuesta = bot.responder(mensaje)

        print(f"\nBIRR-IA: {respuesta}")

    except Exception as error:

        print(f"\nOcurrió un error: {error}")