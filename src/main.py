import flet as ft
from flet_audio import Audio
import threading

# Normalizar teclas
def normalizar_tecla(k: str) -> str:
    k = (k or "").lower()
    if k == "space":
        return " "
    return k.replace(" ", "").replace("-", "")

