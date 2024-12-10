from manim import *

class Hilo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = ORIGIN  
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
        self.joinedby = []  

    def juntar(self):
        self.total.add(self.linea, self.label)
        
    def add_start(self, start):
        self.starts.append(start)
        self.total.add(start)
        self.count += 1

    def add_sleep(self, sleep, n):
        self.sleeps.append(sleep)
        self.total.add(sleep)
        self.count += n
    
    def add_await(self, await_):
        self.awaits.append(await_)
        self.total.add(await_)
        self.count += 1
    
    def add_join(self, join):
        self.joins.append(join)
        self.total.add(join)
        self.count += 1

    def add_signal(self, signal):
        self.signals.append(signal)
        self.total.add(signal)
        self.count += 1

    def add_critica(self, critica):
        self.criticas.append(critica)
        self.total.add(critica)
        self.count += 1

    
        

    '''def juntar(self):
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
    '''

class Semaforo(Hilo):
    def __init__(self, nombre, recursos):
        super().__init__(nombre)
        self.recursos = recursos
        self.cola = []