import flet as ft
from flet_audio import Audio
import threading

# Normalizar teclas
def normalizar_tecla(k: str) -> str:
    k = (k or "").lower()
    if k == "space":
        return " "
    return k.replace(" ", "").replace("-", "")
#PARTE 3 Funcion para mostrar la nota
def mostrar_nota_visual(pagina, teclado, label, nombre_nota, texto_mostrar, recursos, teclado_base):
    img_url = recursos.get(nombre_nota, {}).get("img")
    if not img_uri:
        return
    teclado.src = img_uri
    label.value = f"🎵 (texto_mostrar) 🎵"
    label.visible = True
    pagina.update()
    
    
    def resetear():
        teclado.src = teclado_base
        label.visible = False
        pagina.update()
    threading.Timer(0.5, resetear).start()

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

# PARTE 7 Tabla De Busqueda 
tecla_a_nota = {}
for n in NOTAS:
    for t in n["teclas"]:
        tecla_a_nota[normalizar_tecla(t)] = {"nombre": n["nombre"], "mostrar": n["mostrar"]}
        
# PARTE 7.2 Audios
nombre_a_audio = {}
for nombre, uris in RECURSOS.items():
    reproducir = Audio(src=urls["wat"])
    nombre_a_audio[onmbre] = reproducir
    pagina.overlay.oppend/reproducir
    pagina.overlay.append(reproducir)    