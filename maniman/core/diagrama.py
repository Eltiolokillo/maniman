from maniman.core.auxiliares import *
from maniman.core.objetos import *
from maniman.scenes.escena import Escena
from PIL import Image

class Diagrama:
    """
    N_hilos: cuenta main pero no semaforos. Sirve para saber coordenada x de hilos
    N_semaforos: coordenada x de semaforos
    Acciones: acciones del programa: start, join, sleep, await, end etc.
    Elementos: acciones + tramos para convertir a Manim
    """
    def __init__(self):
        self.n_hilos = 0
        self.n_semaforos = 0
        self.hilos = []
        self.new_hilos = []
        self.semaforos = []
        self.acciones = []
        self.elementos = []
        self.grupos = []

    """
    Se crea hilo que empieza arriba (x = 0)
    """
    def new_thread(self, name):
        hilo = Hilo(name)
        hilo.x = self.n_hilos
        hilo.y = 0
        hilo.empezado = True
        self.n_hilos += 1
        self.hilos.append(hilo)
        self.new_hilos.append(hilo)
        hilo.inicio_tramo(0, 'bien')
        return hilo

    def new_semaphore(self, name, value):
        s = Semaforo(name, value)
        s.x = self.n_semaforos
        self.n_semaforos += 1
        self.semaforos.append(s)
        s.inicio_tramo(0, 'bien')
        return s

    def accion(self, hilo, text):
        a = Unaria(hilo, text)
        hilo.objetos.append(a)
        self.acciones.append(a)
        hilo.t += 1
        return a

    def start(self, hilo, name):
        creado = Hilo(name)
        s = Start(hilo, creado)
        creado.x = self.n_hilos
        creado.y = hilo.t
        hilo.t += 1
        creado.t = hilo.t
        self.n_hilos += 1
        hilo.objetos.append(s)
        self.acciones.append(s)
        self.hilos.append(creado)
        return creado
    
    def sleep(self, hilo, d):
        s = Sleep(hilo, d)
        hilo.t += d
        hilo.objetos.append(s)
        self.acciones.append(s)
    
    def await_(self, hilo, sem):
        a = Await(hilo, sem)
        hilo.t += 1
        hilo.objetos.append(a)
        self.acciones.append(a)

    def signal(self, hilo, sem):
        s = Signal(hilo, sem)
        hilo.t += 1
        hilo.objetos.append(s)
        self.acciones.append(s)

    def join(self, hilo, destino):
        j = Join(hilo, destino)
        hilo.t += 1
        hilo.objetos.append(j)
        self.acciones.append(j)
        destino.joinedby.append(hilo)

    def end(self, hilo):
        e = End(hilo)
        hilo.t += 1
        hilo.objetos.append(e)
        self.acciones.append(e)

    def crear_escena(self):
        procesar(self)
        g = a_manim(self)
        scene = Escena(g)
        scene.render()

    def guardar_imagen_final(scene, file_path="media\\videos\\1080p60\\escena.png"):
        # Obtén el fotograma final de la escena
        frame = scene.renderer.get_frame()
        # Convierte el fotograma en una imagen de Pillow
        image = Image.fromarray(frame)
        # Guarda la imagen, sobrescribiendo el archivo si ya existe
        image.save(file_path)