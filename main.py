import json
from manim import *
from maniman.escena import Escena
from maniman.hilo import Hilo
from maniman.modificador import Modificador
from maniman.pintor import Pintor
from maniman.hilo import *
from PIL import Image

import os

# Calidad de la animación
config.quality = "high_quality"


# Cargar fichero con configuración de apariencias
def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
config = load_config("config.json")


grupo = VGroup()

def main():

    # Todo dibujo tiene main y semaforo. Este último se puede ocultar
    a = Hilo("a")
    b = Hilo("b")
    c = Hilo("c")
    hilos = [a, b, c]

    # Crear main
    main = Hilo("main")
    main.posicion = ORIGIN + UP*1
        
    # Posicionar dinámicamente los hilos
    for i, hilo in enumerate(hilos):
        hilo.posicion = RIGHT * (i+1) * 2

     # Crear y posicionar el semáforo
    recursos = 1
    semaforo = Hilo(f"sem={recursos}")
    semaforo.posicion = RIGHT * ((len(hilos)+1) * 2)

    
    # Instanciar herramientas
    show_semaf = True
    cola = []
    md = Modificador()
    pt = Pintor(md, show_semaf, recursos, cola)
        
    # Dibujar hilos y semáforo
    for hilo in [main] +  hilos:
        pt.dibujar_hilo(hilo)

    if show_semaf:
        pt.dibujar_hilo(semaforo)
        

    # Acciones main
    pt.start(main,a)
    pt.start(main,b)
    pt.join(main,a)
    pt.join(main,b)
        
    # Acciones en los hilos
    pt.await_(a,semaforo)
    pt.start(a, c)
    pt.sleep(a, 2)
    #pt.signal(a,semaforo)
    pt.join(a, c)
    md.end(a)

    pt.critic(b)
    md.end(b)

    pt.await_(c,semaforo)
    pt.critic(c)
    pt.signal(c,semaforo)
    md.end(c)


    #md.agitar(hilos + [main])
        
    # Grupo principal
    grupo = VGroup(*[hilo.total for hilo in [main] + [semaforo] + hilos])
    

    # Renderizar la escena
    scene = Escena(grupo)
    scene.render()
    guardar_imagen_final(scene, file_path="media\\videos\\1080p60\\escena.png")

def guardar_imagen_final(scene, file_path="media\\videos\\1080p60\\escena.png"):
    # Obtén el fotograma final de la escena
    frame = scene.renderer.get_frame()
    # Convierte el fotograma en una imagen de Pillow
    image = Image.fromarray(frame)
    # Guarda la imagen, sobrescribiendo el archivo si ya existe
    image.save(file_path)


if __name__ == "__main__":
    main()