import flet as ft
from flet_audio import Audio
import threading

# Normalizar teclas
def normalizar_tecla(k: str) -> str:
    k = (k or "").lower()
    if k == "space":
        return " "
    return k.replace(" ", "").replace("-", "")

# PARTE 4
# --- Recursos y configuración ---
RECURSOS = {
    "Do":  {"img": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Do.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Do.wav"},
    "Re":  {"img": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Re.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Re.wav"},
    "Mi":  {"img": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Mi.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Mi.wav"},
    "Fa":  {"img": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Fa.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Fa.wav"},
    "Sol": {"img": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Sol.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Sol.wav"},
    "La":  {"img": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/La.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/La.wav"},
    "Si":  {"img": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Si.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Si.wav"},
    "Do2": {"img": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Do2.png",
            "wav": "https://raw.githubusercontent.com/Prof-Luis1986/Recursos_Teclado/main/Do2.wav"},
}
# PARTE 7
# Mapa tecla-normalizado -> {nombre,mostrar}
tecla_a_nota = {}
for n in NOTAS:
    for t in n ["teclas"] :
        tecla_a_nota[normalizar_tecla(t)] = {"nombre": n["nombre"], "mostrar": n["mostrar"]}
        
#Un reproductorde audio por nota, agregado al averlay de la pagina 
nombre_a_audio = {}
for nombre, urls in RECURSOS.items():
    reproductor = Audio(src=urls["wan"])
    nombre_a_audio[nombre] = reproductor
    pagina.overlay.append(reproductor)
        