from manim import *

class Hilo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = ORIGIN  # Posición inicial (se ajustará dinámicamente)
        self.linea = None
        self.label = None
        self.starts = []
        self.sleeps = []
        self.awaits = []
        self.joins = []
        self.signals = []
        self.criticas = []
        self.total = VGroup()
        self.count = 1
        self.joinedby = []  # Lista de hilos que hacen join sobre este

    def juntar(self):
        # Usamos un set para evitar duplicados
        elementos_unicos = set(
            [self.linea, self.label]
            + [item for sublist in self.starts for item in sublist]
            + [item for sublist in self.sleeps for item in sublist]
            + [item for sublist in self.awaits for item in sublist]
            + [item for sublist in self.joins for item in sublist]
            + [item for sublist in self.signals for item in sublist]
            + [item for sublist in self.criticas for item in sublist]
        )
        self.total = VGroup(*elementos_unicos)