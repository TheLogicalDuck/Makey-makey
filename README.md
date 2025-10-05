📘 Manual Técnico – Piano Makey Makey (Flet)
📌 Descripción del proyecto
Este proyecto es un Piano digital interactivo desarrollado con Flet y pensado para ser
usado con Makey Makey o el teclado del ordenador.
El programa permite reproducir las notas musicales Do, Re, Mi, Fa, Sol, La, Si, Do2,
mostrando una imagen correspondiente a la tecla presionada y reproduciendo su sonido
asociado.
Su objetivo es simular un teclado musical básico para actividades educativas o
recreativas, combinando interacción física (Makey Makey) con recursos visuales y
auditivos digitales.
🖥Tecnologías usadas
 Python 3.x
 Flet (versión 0.22 o superior)
 flet-audio
 Recursos externos (imágenes y audios desde GitHub)
⚙ Requisitos técnicos
 Python 3.10 o superior.
 Librerías necesarias:
 pip install flet flet-audio
 Conexión a Internet (para cargar imágenes y sonidos desde GitHub).
 (Opcional) Dispositivo Makey Makey conectado al equipo.
<img width="583" height="194" alt="image" src="https://github.com/user-attachments/assets/3e4a0624-97b4-45f5-8b10-aaecfde834dd" />
- Explicación del código
 normalizar_tecla(k):
Limpia y convierte las teclas a un formato estándar para detectar correctamente
las pulsaciones, incluso si vienen desde Makey Makey.
 mostrar_nota_visual(...):
Muestra la imagen correspondiente a la nota presionada y su nombre. Luego de
0.5 segundos, restaura el teclado base.
 RECURSOS:
Diccionario que vincula cada nota musical con su imagen (img) y archivo de
sonido (wav).
 NOTAS:
Lista que define qué teclas del teclado (o Makey Makey) activan cada nota.
 main(pagina):
o Configura la ventana principal de Flet.
o Crea la interfaz visual (imagen del teclado + texto).
o Mapea las teclas a las notas.
o Asocia eventos de teclado para reproducir sonido y cambiar imagen.
🛠 Posibles errores y soluciones
Error Causa Solución
No se escucha sonido Falta de internet o error de
enlace
Verificar conexión o URL de
recursos
Imagen del teclado no
aparece
URL caída o error de carga Revisar enlace a GitHub
No responde al Makey
Makey
Configuración incorrecta de
teclas
Verificar mapeo en la
variable NOTAS
Audio no se reproduce en
Windows
Falta del módulo fletaudio
Ejecutar pip install
flet-audio
🚀 Cómo ejecutar
1. Asegúrate de tener Python y las librerías instaladas.
2. Guarda el archivo como main.py.
3. Ejecuta el proyecto desde la terminal:
4. flet run main.py
5. Presiona las teclas Q W E R T Y U I o usa el Makey Makey configurado con
esas entradas para tocar las notas.

👤 Manual de Usuario – Piano Makey Makey (Flet)
🎯 Descripción de la app
El Piano Makey Makey es una aplicación interactiva que permite tocar notas musicales
desde el teclado o mediante el dispositivo Makey Makey.
Cada tecla presionada muestra la nota correspondiente en pantalla y reproduce su sonido
real.
🖥 Requisitos de uso
 Tener Python 3.10+ instalado.
 Instalar las librerías:
 pip install flet flet-audio
 (Opcional) Contar con un Makey Makey configurado para las teclas musicales.
▶ Pasos para ejecutar
1. Descargar o clonar el proyecto desde GitHub o la carpeta compartida.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:
4. flet run main.py
5. Esperar a que se abra la ventana del piano.
🎹 Instrucciones de uso
Nota Teclas del teclado Sonido
Do Q / Z do.wav
Re W / X re.wav
Mi E / C mi.wav
Fa R / V fa.wav
Sol T / B sol.wav
La Y / N la.wav
Si U / M si.wav
Nota Teclas del teclado Sonido
Do2 I / , do2.wav
Pasos:
1. Presiona una de las teclas indicadas.
2. Observa cómo cambia la imagen del teclado mostrando la nota.
3. Escucha el sonido correspondiente.
4. Usa combinaciones rápidas para crear melodías simples.
📸 Ejemplo visual
🎵 Al presionar la tecla "Q" se muestra la nota "Do" y se escucha su
sonido 🎵
(Se pueden agregar capturas mostrando las imágenes Do, Re, Mi…)
<img width="1266" height="713" alt="MAKEY 1" src="https://github.com/user-attachments/assets/39d1f944-99da-4099-bcb5-490da56c75f6" />
<img width="1266" height="713" alt="MAKEY 2" src="https://github.com/user-attachments/assets/d101b0a2-3ade-43da-8cb6-12142afb4f7b" />
<img width="1266" height="713" alt="MAKEY 3" src="https://github.com/user-attachments/assets/93581ccb-a500-4e47-9317-2122227b8201" />
<img width="1266" height="713" alt="MAKEY 4" src="https://github.com/user-attachments/assets/10771c61-23eb-4bf3-8e01-3974968b482c" />
❌ Errores comunes
Problema Solución
No se escucha ninguna nota Verifica la conexión a Internet o el módulo flet-audio.
No cambia la imagen del
teclado Revisa si la URL del recurso sigue activa.
Makey Makey no responde Revisa las conexiones de cables o el mapeo de teclas en el
código.
Ventana no abre Asegúrate de tener Flet correctamente instalado.

Diagrama sencillo:
<img width="263" height="377" alt="image" src="https://github.com/user-attachments/assets/591bb971-29dc-4fc9-9b48-55dd8c3bc1a0" />
