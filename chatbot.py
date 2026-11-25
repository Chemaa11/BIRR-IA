from gemini_api import generar_respuesta


class Chatbot:

    def __init__(self):
        self.historial = []

        self.perfil = {
            "nombre": "",
            "carrera": "",
            "objetivo": ""
        }

    # Configurar el perfil del usuario
    def configurar_perfil(self, nombre, carrera, objetivo):

        self.perfil["nombre"] = nombre
        self.perfil["carrera"] = carrera
        self.perfil["objetivo"] = objetivo

    # Enviar mensajes al chatbot
    def responder(self, mensaje):

        contexto = f"""
        Eres BIRR-IA, un asistente inteligente
        desarrollado con Google Gemini.

        Tu objetivo es ofrecer ayuda personalizada,
        consejos académicos y explicaciones claras.

        PERFIL DEL USUARIO:
        Nombre: {self.perfil['nombre']}
        Carrera: {self.perfil['carrera']}
        Objetivo: {self.perfil['objetivo']}

        INSTRUCCIONES:
        - Responde en español.
        - Sé amable, claro y profesional.
        - Adapta tus respuestas al perfil del usuario.
        - Recuerda el contexto de la conversación.
        - Ofrece ejemplos cuando sea necesario.
        - No inventes información.
        - Reconoce cuando no conozcas una respuesta.

        HISTORIAL DE CONVERSACIÓN:
        """

        # Recuperar los últimos 10 mensajes
        for elemento in self.historial[-10:]:

            contexto += (
                f"\n{elemento['rol']}: "
                f"{elemento['contenido']}\n"
            )

        contexto += f"\nUsuario: {mensaje}\n"
        contexto += "\nBIRR-IA:"

        # Obtener respuesta de Gemini
        respuesta = generar_respuesta(contexto)

        if not respuesta:
            raise RuntimeError(
                "Gemini no devolvió una respuesta de texto."
            )

        # Guardar mensaje del usuario
        self.historial.append({
            "rol": "Usuario",
            "contenido": mensaje
        })

        # Guardar respuesta del chatbot
        self.historial.append({
            "rol": "BIRR-IA",
            "contenido": respuesta
        })

        return respuesta

    # Obtener historial
    def obtener_historial(self):
        return self.historial

    # Limpiar conversación
    def limpiar_historial(self):
        self.historial = []