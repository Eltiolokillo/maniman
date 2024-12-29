from manim import *

import copy

from objetos import *
from escena import *


class Diagrama:
    def __init__(self):
        self.n_hilos = 0
        self.n_semaforos = 0
        self.hilos = []
        self.semaforos = []
        self.acciones = []

    def new_thread(self, name):
        hilo = Hilo(name)
        hilo.x = self.n_hilos
        hilo.y = 0
        self.n_hilos += 1
        self.hilos.append(hilo)
        return hilo

    def new_semaphore(self, name, value):
        self.n_semaforos += 1
        s = Semaforo(name, value)
        self.semaforos.append(s)
        return s

    def accion(self, hilo, text):
        a = Accion(hilo, text)
        hilo.objetos.append(a)
        self.acciones.append(a)
        hilo.t += 1
        return a

    def start(self, hilo, name):
        s = Start(hilo, name)
        creado = Hilo(name)
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

    def print_diagrama(self):
        for hilo in self.hilos:
            print(f"HILO: {hilo.nombre}\n")
            for obj in hilo.objetos:
                if isinstance(obj, Accion):
                    print(f"Accion: t = {obj.t}")
                elif isinstance(obj, Start):
                    print(f"Start: t = {obj.t}")
                elif isinstance(obj, Sleep):
                    print(f"Sleep: t = {obj.t}")
                elif isinstance(obj, Await):
                    print(f"Await: t = {obj.t}")
                elif isinstance(obj, Signal):
                    print(f"Signal: t = {obj.t}")
                elif isinstance(obj, Join):
                    print(f"Join: t = {obj.t}")
                elif isinstance(obj, End):
                    print(f"End: t = {obj.t}")
            print("\n")

    def print_acciones(self):
        for accion in self.acciones:
            print(f"Tipo: {accion}, origen: {accion.hilo.nombre}, t: {accion.t}")

    def ordenar(self):
        self.acciones.sort(key=lambda accion: accion.t)
        for accion in self.acciones:
            print(f"Tipo: {accion}, origen: {accion.hilo}, t: {accion.t}")

    def ajustarTiempos(self):
        '''
        Se ordenan las acciones y se recorren una a una, siempre y cuando no
        estén bloqueadas. Se bloquean con awaits y joins, y se liberan con
        signals y ends. Si están bloqueadas se encolan. Al desbloquear, todas
        las acciones de la cola vuelven a la lista global pero con tiempo actualizado
        t_nuevo = t_desbloqueo + t_antiguo 
        '''
        bloqueados = []         # Lista de hilos bloqueados
        cola = []               # Cola de acciones
        final = []              # Lista de acciones finales
        t = 0                   # Tiempo actual
        copia = self.acciones    # Copia de las acciones para no modificar la original
        while copia and t < 15:
            print(f"\nTIEMPO: {t}")
            print("HILOSBLOQUEADS: ")
            for hilo in bloqueados:
                print(hilo.nombre)
            print("COLA: ")
            for accion in cola:
                print(f"TIPO: {accion}, ORIGEN: {accion.hilo.nombre}, TIEMPO: {accion.t}")
            print("COPIA:")
            for accion in copia:
                print(f"TIPO: {accion}, ORIGEN: {accion.hilo.nombre}, TIEMPO: {accion.t}")
            print("FINAL:")
            for accion in final:
                print(f"TIPO: {accion}, ORIGEN: {accion.hilo.nombre}, TIEMPO: {accion.t}")
            for accion in copia:
                # Cada accion que se ejecuta en t
                if accion.t == t:
                    # Si la accion no esta bloqueada
                    print(f"ACCION.HILO: {accion.hilo.nombre}")
                    if not(accion.hilo in bloqueados):
                        final.append(accion)
                        # Await: Si hay recursos, resta.
                        # Si no hay recursos, bloquea y encola.
                        if isinstance(accion, Await):
                            if accion.semaforo.recursos > 0:
                                accion.semaforo.recursos -= 1
                            else:
                                bloqueados.append(accion.hilo)
                        # Signal: Si hay hilos bloqueados, desbloquea al primero.
                        # Si no hay hilos bloqueados, libera recurso.
                        if isinstance(accion, Signal):
                            if bloqueados:
                                hilo = bloqueados.pop(0)
                                for desbloqueada in cola:
                                    if desbloqueada.hilo == hilo:
                                        desbloqueada.t = t + (desbloqueada.t_bloqueo - hilo.bloqueado_en)
                                        copia.append(desbloqueada)
                            else:
                                accion.semaforo.recursos += 1
                        # Join: Si el hilo al que se une no ha terminado, bloquea.
                        # Si ha terminado, sigue.
                        if isinstance(accion, Join):
                            # Si NO ha ocurrido un end de el hilo al que se une, bloquea
                            if not(any(isinstance(obj, End) and obj.hilo == accion.destino for obj in final)):
                                #print(f"Bloqueando a: {accion.hilo.nombre}")
                                accion.hilo.bloqueado_en = t+1
                                bloqueados.append(accion.hilo)
                                #print(f"Cola: {cola}")
                                #print(f"Bloqueados: {bloqueados}")
                        # End: Libera recurso
                        if isinstance(accion, End):
                            '''
                            Para cada hilo bloqueado, si es un hilo que esperaba a este lo desbloquea.
                            Luego recorre la cola y las acciones desbloqueadas vuelven a la lista global
                            '''
                            for hilo in bloqueados:
                                if hilo in accion.hilo.joinedby:
                                    print(f"Desbloqueando a: {hilo.nombre} en tiempo: {t}")     
                                    bloqueados.remove(hilo)
                                    max = 0
                                    eliminar_de_cola = []   
                                    agregar_a_copia = []   
                                    for desbloqueada in cola:
                                        print(f"TIPO: {desbloqueada}, ORIGEN: {desbloqueada.hilo.nombre}, TIEMPO: {desbloqueada.t}")
                                        if desbloqueada.hilo == hilo:
                                            if max < (desbloqueada.t_bloqueo - hilo.bloqueado_en + 1):
                                                max = desbloqueada.t_bloqueo - hilo.bloqueado_en 
                                            desbloqueada.t = t + (desbloqueada.t_bloqueo - hilo.bloqueado_en) + 1
                                            if desbloqueada.t == t:
                                                print("TIEMPO ERA GUAL, REVISEN")
                                                desbloqueada.t += 1
                                            agregar_a_copia.append(desbloqueada)
                                            print("APEDADO")
                                            eliminar_de_cola.append(desbloqueada)
                                            print(f"Accion que vuelve: Tipo: {desbloqueada}, origen: {desbloqueada.hilo.nombre}, t: {desbloqueada.t}") 
                                    for accion in copia:
                                        if accion.hilo == hilo:
                                            accion.t = accion.t + max
                                    for accion in eliminar_de_cola:
                                        cola.remove(accion) 
                                    for accion in agregar_a_copia:
                                        copia.append(accion)
                        copia.remove(accion)
                    # Si está bloqueada se encola
                    else:
                        accion.t_bloqueo = t
                        cola.append(accion)
                        print(f"ENCOLANDO; Accion: {accion}, origen: {accion.hilo.nombre}, t: {accion.t}, t_bloqueo: {accion.t_bloqueo}")
                        copia.remove(accion)
            t += 1
        self.acciones = final
        print(f"COLAFINAL: {cola}")
                        

