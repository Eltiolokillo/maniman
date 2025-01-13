from typing import Any
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
        self.bloqueado_desde = 0
        self.empezado = False
        self.acabado = False
        self.tramos = []

    def inicio_tramo(self, t, tipo):
        if self.tramos and self.tramos[-1].final is None:
            raise ValueError("Ya hay un tramo iniciado sin finalizar.")
        self.tramos.append(Tramo(t,tipo))  # Añade el inicio del tramo con tipo

    def fin_tramo(self, t):
        if not self.tramos or self.tramos[-1].final is not None:
            raise ValueError("No hay un tramo iniciado para terminar.")
        self.tramos[-1].final = t  # Establece el fin del último tramo iniciado

    def imprimir_tramos(self):
        """
        Imprime todos los tramos del hilo con su información.
        """
        if not self.tramos:
            print(f"Hilo {self.nombre} no tiene tramos registrados.")
        else:
            print(f"Tramos del Hilo {self.nombre}:")
            for i, tramo in enumerate(self.tramos, 1):
                inicio = tramo.t
                fin = tramo.final if tramo.final is not None else "No finalizado"
                tipo = tramo.tipo
                print(f"  Tramo {i}: Inicio={inicio}, Fin={fin}, Tipo={tipo}")

class Tramo:
    def __init__(self, inicio, tipo):
        self.t = inicio
        self.final = None
        self.tipo = tipo
        self.hilo = None

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
        self.acciones_encola = []
        self.estado = 'libre'

    def cambiar_semaforo(self, nuevos_recursos, t, accion):
        tipo_nuevo = "bien" if nuevos_recursos > 0 else "bloq"
        ch = 1 if nuevos_recursos > 0 else -1

        # Si ultimo tramo es distinto al nuevo lo cambia
        if not self.tramos[-1].tipo == tipo_nuevo:
            accion.cambio = ch
            # Finaliza el tramo actual y comienza uno nuevo con el nuevo tipo
            if self.tramos and self.tramos[-1].final is None:
                self.fin_tramo(t)
                self.inicio_tramo(t, tipo_nuevo)

class Accion:
    def __init__(self, hilo, t):
        self.hilo = hilo
        self.t = t
        self.t_bloqueo = 0

class Unaria(Accion):
    def __init__(self, hilo, texto):
        super().__init__(hilo, hilo.t)
        self.texto = texto

class Start(Accion):
    def __init__(self, origen, destino):
        super().__init__(origen, origen.t)
        self.destino = destino

class Sleep(Accion):
    def __init__(self, origen, d):
        super().__init__(origen, origen.t)
        self.duracion = d

class Await(Accion):
    def __init__(self, origen, destino):
        super().__init__(origen, origen.t)
        self.semaforo = destino
        self.t_bloqueo = 0
        self.recurso_final = 0
        self.cola_final = []
        self.cambio = 0

class Signal(Accion):
    def __init__(self, origen, destino):
        super().__init__(origen, origen.t)
        self.semaforo = destino
        self.t_bloqueo = 0
        self.recurso_final = 0
        self.cola_final = []
        self.cambio = 0
        self.desbloquea_a = None

class Join(Accion):
    def __init__(self, origen, destino):
        super().__init__(origen, origen.t)
        self.destino = destino

class End(Accion):
    def __init__(self, origen):
        super().__init__(origen, origen.t)
