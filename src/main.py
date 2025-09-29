import flet as ft
from flet_audio import Audio
import threading

# --- Normalizar teclas ---
def normalizar_tecla(k: str) -> str:
    k = (k or "").lower()
    if k == "space":
        return " "
    return k.replace(" ", "").replace("-", "")

# --- Mostrar nota (recibe pagina, teclado y label como argumentos) ---
def mostrar_nota_visual(pagina, teclado, label, nombre_nota, texto_mostrar, recursos, teclado_base):
    img_url = recursos.get(nombre_nota, {}).get("img")
    if not img_url:
        return
    teclado.src = img_url
    label.value = f"🎵 {texto_mostrar} 🎵"
    label.visible = True
    pagina.update()

    def resetear():
        teclado.src = teclado_base
        label.visible = False
        pagina.update()
    threading.Timer(0.5, resetear).start()


# --- Configuración de recursos y notas ---
RECURSOS = {
    "Do":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado do.png",
            "wav": "ALL-THE-KEYBOARD-RESOURCES/AUDIO/do.wav"},
    "Re":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado re.png",
            "wav": "ALL-THE-KEYBOARD-RESOURCES/AUDIO/re.wav"},
    "Mi":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado mi.png",
            "wav": "ALL-THE-KEYBOARD-RESOURCES/AUDIO/mi.wav"},
    "Fa":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado fa.png",
            "wav": "ALL-THE-KEYBOARD-RESOURCES/AUDIO/fa.wav"},
    "Sol": {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado sol.png",
            "wav": "ALL-THE-KEYBOARD-RESOURCES/AUDIO/sol.wav"},
    "La":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado la.png",
            "wav": "ALL-THE-KEYBOARD-RESOURCES/AUDIO/la.wav"},
    "Si":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado si.png",
            "wav": "ALL-THE-KEYBOARD-RESOURCES/AUDIO/si.wav"},
    "Do2": {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado do2.png",
            "wav": "ALL-THE-KEYBOARD-RESOURCES/AUDIO/do2.wav"},
}

TECLADO_BASE = "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado base.png"

NOTAS = [
    {"nombre": "Do",   "mostrar": "Do", "teclas": ["w"]},
    {"nombre": "Re",   "mostrar": "Re", "teclas": ["a"]},
    {"nombre": "Mi",   "mostrar": "Mi", "teclas": ["s"]},
    {"nombre": "Fa",   "mostrar": "Fa", "teclas": ["d"]},
    {"nombre": "Sol",  "mostrar": "Sol","teclas": ["f"]},
    {"nombre": "La",   "mostrar": "La", "teclas": ["g"]},
    {"nombre": "Si",   "mostrar": "Si", "teclas": [" ", "space"]},
    {"nombre": "Do2",  "mostrar": "Do", "teclas": ["arrowright", "arrow right", "arrow-right"]},
]


# --- Main (queda lo último) ---
def main(pagina: ft.Page):
    pagina.title = "Piano Makey Makey"
    pagina.bgcolor = "black"
    pagina.window_width = 800
    pagina.window_height = 450

    teclado = ft.Image(src=TECLADO_BASE, width=800, height=300)
    nota_label = ft.Text("", size=40, color="yellow", weight="bold",
                         text_align="center", visible=False)

    pagina.add(
        ft.Column(
            [
                ft.Container(content=nota_label, alignment=ft.alignment.center, height=100),
                teclado,
            ],
            alignment="center",
            horizontal_alignment="center",
        )
    )

    # Mapear teclas y audios
    tecla_a_nota = {}
    for n in NOTAS:
        for t in n["teclas"]:
            tecla_a_nota[normalizar_tecla(t)] = {"nombre": n["nombre"], "mostrar": n["mostrar"]}

    nombre_a_audio = {}
    for nombre, urls in RECURSOS.items():
        reproductor = Audio(src=urls["wav"])
        nombre_a_audio[nombre] = reproductor
        pagina.overlay.append(reproductor)

    # Evento de teclado
    def al_presionar_tecla(evento: ft.KeyboardEvent):
        tecla_norm = normalizar_tecla(evento.key)
        nota_info = tecla_a_nota.get(tecla_norm)
        if nota_info:
            nombre_nota = nota_info["nombre"]
            texto_mostrar = nota_info["mostrar"]
            reproductor = nombre_a_audio.get(nombre_nota)
            if reproductor:
                reproductor.play()
                mostrar_nota_visual(pagina, teclado, nota_label, nombre_nota, texto_mostrar, RECURSOS, TECLADO_BASE)

    pagina.on_keyboard_event = al_presionar_tecla
    pagina.update()

ft.app(target=main)