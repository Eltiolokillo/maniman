import json
from manim import *
from escena import *
from objetos import *
from modificador import *
from diagrama import *
from PIL import Image
from diagrama import *

from config import visuals

import os

# Calidad de la animación
config.quality = "high_quality"

grupo = VGroup()

def main():
    d1 = Diagrama()
    main = d1.new_thread("main")
    b = d1.start(main, "b")
    s1 = d1.new_semaphore("s1", 1)
    d1.join(main, b)
    d1.accion(main, "t1")
    d1.accion(main, "pen")
    a = d1.start(main, "a")
    d1.join(main,a)
    d1.accion(main,"t2")
    d1.await_(main, s1)
    d1.accion(main, "s1")
    d1.accion(main, "s2")

    d1.await_(a, s1)
    d1.signal(a, s1)
    d1.end(a)

    d1.await_(b, s1)
    d1.sleep(b, 2)
    d1.end(b)

    d1.print_acciones()

    print("\nEYOOOO\n")

    d1.ajustarTiempos()

    d1.print_acciones()

    
    # Renderizar la escena
    #scene = Escena(grupo)
    #scene.render()
    #guardar_imagen_final(scene, file_path="media\\videos\\1080p60\\escena.png")

def guardar_imagen_final(scene, file_path="media\\videos\\1080p60\\escena.png"):
    # Obtén el fotograma final de la escena
    frame = scene.renderer.get_frame()
    # Convierte el fotograma en una imagen de Pillow
    image = Image.fromarray(frame)
    # Guarda la imagen, sobrescribiendo el archivo si ya existe
    image.save(file_path)



if __name__ == "__main__":
    main()

