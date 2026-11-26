from gtts import gTTS
from io import BytesIO


def generar_voz(texto):
    audio = BytesIO()

    voz = gTTS(
        text=texto,
        lang="es",
        tld="com.mx",
        slow=False
    )

    voz.write_to_fp(audio)
    audio.seek(0)

    return audio