from gemini_api import generar_respuesta
from pathlib import Path
from datetime import datetime


class GeneradorCreativo:

    def __init__(self):

        self.ultimo_contenido = ""
        self.ultimo_tipo = ""

        self.tipos = {
            "codigo": """
                Eres un programador experto.
                Genera código funcional, organizado
                y con comentarios explicativos.
                Incluye instrucciones de ejecución
                y explica cómo funciona el código.
            """,

            "script": """
                Eres un especialista en automatización.
                Genera scripts claros y eficientes.
                Explica los requisitos, funcionamiento
                y pasos para ejecutarlos.
            """,

            "musica": """
                Eres un compositor musical creativo.
                Genera composiciones originales,
                letras, acordes, ritmo, tempo
                y estructura musical en texto.
            """,

            "historia": """
                Eres un escritor creativo.
                Genera historias originales con
                personajes, escenarios, desarrollo
                y un desenlace interesante.
            """,

            "guion": """
                Eres un guionista profesional.
                Genera guiones organizados en escenas,
                diálogos, personajes y descripciones.
            """,

            "ideas": """
                Eres un especialista en innovación.
                Genera ideas originales, útiles
                y creativas.
                Explica cómo podrían desarrollarse.
            """
        }

    # Generar contenido creativo
    def generar(self, tipo, descripcion,
                estilo="Profesional",
                extension="Media"):

        if tipo not in self.tipos:
            raise ValueError(
                "El tipo de contenido no es válido."
            )

        if not descripcion.strip():
            raise ValueError(
                "Debes escribir una descripción."
            )

        instrucciones = self.tipos[tipo]

        prompt = f"""
        Eres BIRR-IA, un generador inteligente
        de contenido creativo.

        INSTRUCCIONES ESPECIALIZADAS:
        {instrucciones}

        SOLICITUD DEL USUARIO:
        {descripcion}

        ESTILO:
        {estilo}

        EXTENSIÓN:
        {extension}

        REQUISITOS GENERALES:
        - Genera contenido original.
        - Responde en español.
        - Organiza claramente la información.
        - Adapta el resultado a la solicitud.
        - Evita información inventada presentada
          como si fuera un hecho comprobado.
        """

        resultado = generar_respuesta(prompt)

        if not resultado or not resultado.strip():
            raise RuntimeError(
                "Gemini no generó contenido."
            )

        self.ultimo_contenido = resultado
        self.ultimo_tipo = tipo

        return resultado

    # Mejorar el contenido generado
    def mejorar(self, instrucciones):

        if not self.ultimo_contenido:
            raise ValueError(
                "Primero debes generar contenido."
            )

        prompt = f"""
        Eres BIRR-IA, un asistente creativo.

        Mejora el siguiente contenido según
        las instrucciones del usuario.

        CONTENIDO ORIGINAL:

        {self.ultimo_contenido}

        INSTRUCCIONES DE MEJORA:

        {instrucciones}

        Devuelve el contenido completo mejorado.
        """

        resultado = generar_respuesta(prompt)

        if not resultado or not resultado.strip():
            raise RuntimeError(
                "No se pudo mejorar el contenido."
            )

        self.ultimo_contenido = resultado

        return resultado

    # Guardar el contenido en un archivo
    def guardar(self):

        if not self.ultimo_contenido:
            raise ValueError(
                "No hay contenido para guardar."
            )

        carpeta = (
            Path(__file__).resolve().parent
            / "resultados"
        )

        carpeta.mkdir(exist_ok=True)

        fecha = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        nombre = (
            f"{self.ultimo_tipo}_{fecha}.txt"
        )

        ruta = carpeta / nombre

        ruta.write_text(
            self.ultimo_contenido,
            encoding="utf-8"
        )

        return ruta