import flet as ft
from flet_audio import Audio
import threading

# Normalizar teclas
def normalizar_tecla(k: str) -> str:
    k = (k or "").lower()
    if k == "space":
        return " "
    return k.replace(" ", "").replace("-", "")
#PARTE 3

# PARTE 4
# --- Recursos y configuración ---
RECURSOS = {
    "Do":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado do.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Do.wav"},
    "Re":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado re.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Re.wav"},
    "Mi":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado mi.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Mi.wav"},
    "Fa":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado fa.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Fa.wav"},
    "Sol": {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado sol.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Sol.wav"},
    "La":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado la.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/La.wav"},
    "Si":  {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado si.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Si.wav"},
    "Do2": {"img": "ALL-THE-KEYBOARD-RESOURCES/IMAGES/teclado do2.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Do2.wav"},
}