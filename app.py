import streamlit as st
from chatbot import Chatbot
from analizador import AnalizadorPDF
from generador import GeneradorCreativo
from io import BytesIO
import hashlib

# ==========================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ==========================================

st.set_page_config(
    page_title="BIRR-IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILOS PERSONALIZADOS CSS
# ==========================================

st.markdown("""
<style>

    .stApp {
        background-color: #0B1120;
    }

    [data-testid="stSidebar"] {
        background-color: #111B2E;
    }

    .hero {
        background: linear-gradient(
            135deg, #172554, #312E81
        );
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #4338CA;
        margin-bottom: 30px;
    }

    .hero h1 {
        color: #FFFFFF;
        font-size: 45px;
        margin-bottom: 10px;
    }

    .hero p {
        color: #CBD5E1;
        font-size: 18px;
    }

    .tarjeta {
        background-color: #172238;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #334155;
        min-height: 250px;
        margin-bottom: 15px;
    }

    .tarjeta h2 {
        color: #F1F5F9;
        font-size: 23px;
    }

    .tarjeta p {
        color: #CBD5E1;
        font-size: 16px;
    }

    .emoji {
        font-size: 40px;
    }

    .etiqueta {
        color: #A5B4FC;
        font-size: 13px;
        font-weight: bold;
        letter-spacing: 2px;
    }

    .stButton > button {
        background: linear-gradient(
            135deg, #4F46E5, #7C3AED
        );
        color: white;
        border: none;
        border-radius: 10px;
        min-height: 45px;
        font-weight: bold;
        width: 100%;
    }

    .stButton > button:hover {
        color: white;
        border: 1px solid #A5B4FC;
    }

    .pie {
        text-align: center;
        color: #94A3B8;
        padding: 25px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)

# ==========================================
# ESTADO DE NAVEGACIÓN
# ==========================================

# Inicializar las herramientas de inteligencia artificial

if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()

if "analizador" not in st.session_state:
    st.session_state.analizador = AnalizadorPDF()

if "generador" not in st.session_state:
    st.session_state.generador = GeneradorCreativo()

if "perfil_configurado" not in st.session_state:
    st.session_state.perfil_configurado = False

if "resultado_pdf" not in st.session_state:
    st.session_state.resultado_pdf = ""

if "preguntas_pdf" not in st.session_state:
    st.session_state.preguntas_pdf = []

if "identificador_pdf" not in st.session_state:
    st.session_state.identificador_pdf = None




if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"


def cambiar_pagina(pagina):
    st.session_state.pagina = pagina


# ==========================================
# MENÚ LATERAL
# ==========================================

with st.sidebar:

    st.title("🤖 BIRR-IA")

    st.caption("Intelligence without limits")

    st.divider()

    st.markdown("### NAVEGACIÓN")

    opciones = [
        ("🏠 Inicio", "Inicio"),
        ("💬 Chat inteligente", "Chatbot"),
        ("📚 Investigación", "Investigacion"),
        ("✨ Estudio creativo", "Creatividad"),
        ("ℹ️ Acerca de", "Acerca")
    ]

    for etiqueta, pagina in opciones:

        st.button(
            etiqueta,
            key=f"menu_{pagina}",
            on_click=cambiar_pagina,
            args=(pagina,)
        )

    st.divider()

    st.markdown("### Tecnología")

    st.markdown("🧠 Google Gemini API")
    st.markdown("🐍 Python")
    st.markdown("🌐 Streamlit")

    st.divider()

    st.caption("BIRR-IA | Versión 1.0")


# ==========================================
# PÁGINA DE INICIO
# ==========================================

if st.session_state.pagina == "Inicio":

    st.markdown("""
    <div class="hero">
        <span class="etiqueta">
            INTELIGENCIA ARTIFICIAL
        </span>
        <h1>Bienvenido a BIRR-IA</h1>
        <p>
            Tu plataforma inteligente para aprender,
            investigar y transformar ideas en realidad.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Explora nuestras herramientas")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="tarjeta">
            <div class="emoji">💬</div>
            <h2>Chat inteligente</h2>
            <p>
                Conversa con un asistente capaz
                de ofrecer consejos personalizados
                y apoyo académico.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Abrir chatbot",
            key="inicio_chat",
            on_click=cambiar_pagina,
            args=("Chatbot",)
        )

    with col2:

        st.markdown("""
        <div class="tarjeta">
            <div class="emoji">📚</div>
            <h2>Investigación</h2>
            <p>
                Analiza artículos científicos,
                comprende documentos PDF y
                genera resúmenes inteligentes.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Analizar documentos",
            key="inicio_pdf",
            on_click=cambiar_pagina,
            args=("Investigacion",)
        )

    with col3:

        st.markdown("""
        <div class="tarjeta">
            <div class="emoji">✨</div>
            <h2>Estudio creativo</h2>
            <p>
                Genera código, scripts,
                composiciones musicales,
                historias e ideas innovadoras.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Generar contenido",
            key="inicio_creativo",
            on_click=cambiar_pagina,
            args=("Creatividad",)
        )

    st.divider()

    st.subheader("Nuestra plataforma")

    m1, m2, m3 = st.columns(3)

    m1.metric("Herramientas de IA", "3")
    m2.metric("Categorías creativas", "6")
    m3.metric("Motor inteligente", "Gemini")


# ==========================================
# PÁGINA DEL CHATBOT
# ==========================================

elif st.session_state.pagina == "Chatbot":

    st.title("💬 Chat inteligente")

    st.write(
        "Tu asistente personal y académico "
        "impulsado por Google Gemini."
    )

    chatbot = st.session_state.chatbot

    st.divider()

    with st.expander(
        "👤 Configurar perfil personalizado",
        expanded=not st.session_state.perfil_configurado
    ):

        with st.form("formulario_perfil"):

            col1, col2 = st.columns(2)

            with col1:
                nombre = st.text_input(
                    "Nombre",
                    value=chatbot.perfil.get("nombre", "")
                )

            with col2:
                carrera = st.text_input(
                    "Carrera",
                    value=chatbot.perfil.get("carrera", "")
                )

            objetivo = st.text_input(
                "Objetivo académico",
                value=chatbot.perfil.get("objetivo", "")
            )

            configurar = st.form_submit_button(
                "Guardar perfil"
            )

            if configurar:

                if nombre.strip() and carrera.strip() and objetivo.strip():

                    chatbot.configurar_perfil(
                        nombre,
                        carrera,
                        objetivo
                    )

                    st.session_state.perfil_configurado = True

                    st.success(
                        "Perfil configurado correctamente."
                    )

                else:

                    st.warning(
                        "Completa todos los campos."
                    )

    if st.session_state.perfil_configurado:

        st.success(
            f"Perfil activo: "
            f"{chatbot.perfil['nombre']} | "
            f"{chatbot.perfil['carrera']}"
        )

    if st.button("🗑️ Limpiar conversación"):

        chatbot.limpiar_historial()
        st.rerun()

    st.divider()

    # Mensaje de bienvenida

    with st.chat_message("assistant"):

        st.markdown(
            "¡Hola! Soy **BIRR-IA**, tu asistente "
            "inteligente. ¿En qué puedo ayudarte?"
        )

    # Mostrar historial de conversación

    for mensaje in chatbot.obtener_historial():

        rol = (
            "user"
            if mensaje["rol"] == "Usuario"
            else "assistant"
        )

        with st.chat_message(rol):

            st.markdown(mensaje["contenido"])

    # Recibir mensaje del usuario

    mensaje_usuario = st.chat_input(
        "Escribe tu mensaje...",
        disabled=not st.session_state.perfil_configurado
    )

    if mensaje_usuario:

        with st.chat_message("user"):

            st.markdown(mensaje_usuario)

        with st.chat_message("assistant"):

            try:

                with st.spinner("BIRR-IA está pensando..."):

                    respuesta = chatbot.responder(
                        mensaje_usuario
                    )

                st.markdown(respuesta)

            except Exception as error:

                st.error(
                    f"No se pudo generar la respuesta: {error}"
                )

# ==========================================
# PÁGINA DE INVESTIGACIÓN
# ==========================================

elif st.session_state.pagina == "Investigacion":

    st.title("📚 Analizador de investigaciones")

    st.write(
        "Analiza artículos científicos y comprende "
        "información compleja con inteligencia artificial."
    )

    st.divider()

    analizador = st.session_state.analizador

    archivo = st.file_uploader(
        "Selecciona un artículo de investigación",
        type=["pdf"]
    )

    st.caption(
        "El texto extraído del documento será enviado "
        "a Google Gemini cuando solicites un análisis "
        "o realices una pregunta."
    )

    if archivo is not None:

        # Identificar el documento seleccionado

        datos_pdf = archivo.getvalue()

        identificador = hashlib.sha256(
            datos_pdf
        ).hexdigest()

        # Reiniciar resultados si cambia el documento

        if identificador != st.session_state.identificador_pdf:

            st.session_state.analizador = AnalizadorPDF()
            analizador = st.session_state.analizador

            st.session_state.resultado_pdf = ""
            st.session_state.preguntas_pdf = []
            st.session_state.identificador_pdf = identificador

        st.success(
            f"Documento seleccionado: {archivo.name}"
        )

        st.metric(
            "Tamaño del archivo",
            f"{archivo.size / 1024:.2f} KB"
        )

        # Botón de análisis

        if st.button("🔍 Analizar documento"):

            try:

                with st.spinner(
                    "BIRR-IA está analizando el documento..."
                ):

                    analizador.leer_pdf(
                        BytesIO(datos_pdf)
                    )

                    resultado = analizador.analizar()

                    st.session_state.resultado_pdf = resultado
                    st.session_state.preguntas_pdf = []

                st.success(
                    "Análisis completado correctamente."
                )

            except Exception as error:

                st.error(
                    f"Error al analizar el documento: {error}"
                )

        # Mostrar resultados

        if st.session_state.resultado_pdf:

            st.divider()

            informacion = analizador.obtener_informacion()

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Páginas",
                informacion["paginas"]
            )

            col2.metric(
                "Palabras",
                informacion["palabras"]
            )

            col3.metric(
                "Caracteres",
                informacion["caracteres"]
            )

            pestana1, pestana2 = st.tabs([
                "📋 Resultados del análisis",
                "💬 Preguntas sobre el documento"
            ])

            with pestana1:

                st.markdown(
                    st.session_state.resultado_pdf
                )

                st.download_button(
                    label="📥 Descargar análisis",
                    data=st.session_state.resultado_pdf,
                    file_name="analisis_investigacion.txt",
                    mime="text/plain"
                )

            with pestana2:

                st.subheader(
                    "Consulta información del artículo"
                )

                for consulta in st.session_state.preguntas_pdf:

                    with st.chat_message("user"):
                        st.markdown(consulta["pregunta"])

                    with st.chat_message("assistant"):
                        st.markdown(consulta["respuesta"])

                with st.form(
                    "formulario_pregunta_pdf",
                    clear_on_submit=True
                ):

                    pregunta = st.text_input(
                        "Escribe una pregunta sobre el documento"
                    )

                    preguntar = st.form_submit_button(
                        "Preguntar a BIRR-IA"
                    )

                if preguntar:

                    if pregunta.strip():

                        try:

                            with st.spinner(
                                "Buscando información..."
                            ):

                                respuesta = analizador.preguntar(
                                    pregunta
                                )

                            st.session_state.preguntas_pdf.append({
                                "pregunta": pregunta,
                                "respuesta": respuesta
                            })

                            st.rerun()

                        except Exception as error:

                            st.error(
                                f"Error al responder: {error}"
                            )

                    else:

                        st.warning(
                            "Escribe una pregunta."
                        )

    else:

        st.info(
            "Selecciona un documento PDF para comenzar."
        )

# ==========================================
# PÁGINA DEL GENERADOR CREATIVO
# ==========================================

elif st.session_state.pagina == "Creatividad":

    st.title("✨ Estudio creativo")

    st.write(
        "Transforma tus ideas en contenido "
        "con inteligencia artificial."
    )

    st.divider()

    generador = st.session_state.generador

    tipos = {
        "Código de programación": "codigo",
        "Scripts": "script",
        "Música en texto": "musica",
        "Historias": "historia",
        "Guiones": "guion",
        "Ideas creativas": "ideas"
    }

    with st.form("formulario_creativo"):

        tipo = st.selectbox(
            "Tipo de contenido",
            list(tipos.keys())
        )

        descripcion = st.text_area(
            "Describe lo que deseas generar",
            height=180,
            placeholder="Escribe aquí tus ideas..."
        )

        col1, col2 = st.columns(2)

        with col1:

            estilo = st.selectbox(
                "Estilo",
                [
                    "Profesional",
                    "Educativo",
                    "Creativo",
                    "Formal",
                    "Informal",
                    "Técnico",
                    "Pop",
                    "Ciencia ficción",
                    "Innovador"
                ]
            )

        with col2:

            extension = st.selectbox(
                "Extensión",
                ["Corta", "Media", "Larga"],
                index=1
            )

        generar = st.form_submit_button(
            "✨ Generar contenido"
        )

    # Generar contenido con Gemini

    if generar:

        if not descripcion.strip():

            st.warning(
                "Escribe una descripción del contenido."
            )

        else:

            try:

                with st.spinner(
                    "BIRR-IA está creando tu contenido..."
                ):

                    generador.generar(
                        tipos[tipo],
                        descripcion,
                        estilo,
                        extension
                    )

                st.success(
                    "Contenido generado correctamente."
                )

            except Exception as error:

                st.error(
                    f"Error al generar contenido: {error}"
                )

    # Mostrar contenido generado

    if generador.ultimo_contenido:

        st.divider()

        st.subheader("📄 Contenido generado")

        st.caption(
            f"Categoría: {generador.ultimo_tipo}"
        )

        st.markdown(
            generador.ultimo_contenido
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                label="📥 Descargar contenido",
                data=generador.ultimo_contenido,
                file_name=(
                    f"{generador.ultimo_tipo}_BIRR-IA.txt"
                ),
                mime="text/plain"
            )

        with col2:

            if st.button("💾 Guardar en el proyecto"):

                try:

                    ruta = generador.guardar()

                    st.success(
                        "Contenido guardado correctamente."
                    )

                    st.caption(str(ruta))

                except Exception as error:

                    st.error(
                        f"Error al guardar: {error}"
                    )

        st.divider()

        # Mejorar el contenido

        st.subheader("🪄 Mejorar contenido")

        with st.form(
            "formulario_mejora",
            clear_on_submit=True
        ):

            instrucciones = st.text_area(
                "¿Qué deseas mejorar?",
                placeholder=(
                    "Agrega ejemplos, cambia el estilo "
                    "o amplía la explicación..."
                )
            )

            mejorar = st.form_submit_button(
                "Mejorar contenido"
            )

        if mejorar:

            if instrucciones.strip():

                try:

                    with st.spinner(
                        "Mejorando el contenido..."
                    ):

                        generador.mejorar(
                            instrucciones
                        )

                    st.rerun()

                except Exception as error:

                    st.error(
                        f"Error al mejorar: {error}"
                    )

            else:

                st.warning(
                    "Escribe las instrucciones de mejora."
                )

        if st.button("🗑️ Limpiar contenido"):

            st.session_state.generador = GeneradorCreativo()

            st.rerun()

    else:

        st.info(
            "El contenido generado aparecerá aquí."
        )
# ==========================================
# PÁGINA ACERCA DE
# ==========================================

elif st.session_state.pagina == "Acerca":

    st.title("ℹ️ Acerca de BIRR-IA")

    st.markdown("""
    ## ¿Qué es BIRR-IA?

    BIRR-IA es una plataforma de inteligencia
    artificial desarrollada con Python y la
    API de Google Gemini.

    ### Objetivo general

    Desarrollar una aplicación capaz de
    comprender el lenguaje natural, analizar
    información compleja y generar contenido
    creativo mediante inteligencia artificial.

    ### Funcionalidades

    - Chatbot con consejos personalizados.
    - Análisis de artículos de investigación.
    - Generación de contenido creativo.

    ### Tecnologías utilizadas

    - Python.
    - Google Gemini API.
    - Streamlit.
    - PyPDF.
    - Visual Studio Code.

    ### Versión

    1.0 - Proyecto académico en desarrollo.
    """)


# ==========================================
# PIE DE PÁGINA
# ==========================================

st.divider()

st.markdown("""
<div class="pie">
    BIRR-IA | Powered by Google Gemini<br>
    Proyecto de Inteligencia Artificial
</div>
""", unsafe_allow_html=True)