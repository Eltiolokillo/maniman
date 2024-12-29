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
        self.bloqueado_en = 0

    # Redefinir == para que compare nombres
    '''def __eq__(self, other):
        if isinstance(other, Hilo):
            return self.nombre == other.nombre
        return False'''

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
        self.t_bloqueo = 0

class Start:
    def __init__(self, origen, destino):
        self.hilo = origen
        self.t = origen.t
        self.destino = destino
        self.t_bloqueo = 0

class Sleep:
    def __init__(self, origen, d):
        self.hilo = origen
        self.t = origen.t
        self.duracion = d
        self.t_bloqueo = 0

class Await:
    def __init__(self, origen, destino):
        self.hilo = origen
        self.t = origen.t
        self.semaforo = destino
        self.t_bloqueo = 0

class Signal:
    def __init__(self, origen, destino):
        self.hilo = origen
        self.t = origen.t
        self.semaforo = destino
        self.t_bloqueo = 0

class Join:
    def __init__(self, origen, destino):
        self.hilo = origen
        self.t = origen.t
        self.destino = destino
        self.t_bloqueo = 0

class End:
    def __init__(self, origen):
        self.hilo = origen
        self.t = origen.t
        self.t_bloqueo = 0
