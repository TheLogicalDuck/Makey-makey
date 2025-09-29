import flet as ft
from flet_audio import Audio
import threading

# Normalizar teclas
def normalizar_tecla(k: str) -> str:
    k = (k or "").lower()
    if k == "space":
        return " "
    return k.replace(" ", "").replace("-", "")
 # PARTE 5 
# nombre: clave de RECURSOS; mostrar: texto visible en el label; teclas: qué teclas disparan la nota
NOTAS = [
    {"nombre": "Do",   "mostrar": "Do", "teclas": ["w"]},
    {"nombre": "Re",   "mostrar": "Re", "teclas": ["a"]},
    {"nombre": "Mi",   "mostrar": "Mi", "teclas": ["s"]},
    {"nombre": "Fa",   "mostrar": "Fa", "teclas": ["d"]},
    {"nombre": "Sol",  "mostrar": "Sol","teclas": ["f"]},
    {"nombre": "La",   "mostrar": "La", "teclas": ["g"]},
    {"nombre": "Si",   "mostrar": "Si", "teclas": [" ", "space"]},
    # Do agudo: suena con recursos Do2 (imagen/audio), pero en el label mostramos "Do"
    {"nombre": "Do2",  "mostrar": "Do", "teclas": ["arrowright", "arrow right", "arrow-right"]},
]
  # PAERTE 6
def main(pagina: ft.Page):
    # Ventana
    pagina.title = "Piano Makey Makey"
    pagina.bgcolor = "black"
    pagina.window_width = 800
    pagina.window_height = 450
    pagina.window_resizable = False
    pagina.padding = 0
    pagina.spacing = 0

    # Controles base
    teclado = ft.Image(src=TECLADO_BASE, width=800, height=300)
    nota_label = ft.Text(
        value="",
        size=40,
        color="yellow",
        weight="bold",
        text_align="center",
        visible=False,
    )

    # Layout: label arriba, teclado abajo
    pagina.add(
        ft.Column(
            [
                ft.Container(content=nota_label, alignment=ft.alignment.center, height=100),
                teclado,
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=10,
        )
    )
    