from manim import *

class Hilo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.x = 0
        self.y = 0
        self.linea = None
        self.label = None
        self.objetos = []
        self.joinedby = []
        self.t = 1
        self.total = VGroup()

class Semaforo(Hilo):
    def __init__(self, nombre, recursos):
        super().__init__(nombre)
        self.recursos = recursos
        self.bloqueados = []

class Accion:
    def __init__(self, hilo, texto):
        self.hilo = hilo
        self.t = hilo.t
        self.texto = texto

class Start:
    def __init__(self, origen, destino):
        self.hilo = origen
        self.t = origen.t
        self.destino = destino

class Sleep:
    def __init__(self, origen, d):
        self.hilo = origen
        self.t = origen.t
        self.duracion = d

class Await:
    def __init__(self, origen, destino):
        self.hilo = origen
        self.t = origen.t
        self.semaforo = destino

class Signal:
    def __init__(self, origen, destino):
        self.hilo = origen
        self.t = origen.t
        self.semaforo = destino

class Join:
    def __init__(self, origen, destino):
        self.hilo = origen
        self.t = origen.t
        self.destino = destino

class End:
    def __init__(self, origen):
        self.hilo = origen
        self.t = origen.t
