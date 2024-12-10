from manim import *
import json
from random import uniform

from hilo import *
from objetos import *

from config import visuals

class Pintor:
    def __init__(self, md, show_semaf, recursos, cola, grupo):
        self.md = md
        self.show_semaf = show_semaf
        self.recursos = recursos
        self.cola = cola
        self.grupo = grupo
        self.n_hilos = 0
    
    def dibujar_main(self):
        main = Hilo("main")
        main.posicion = ORIGIN + UP*1
        main.linea = Line(ORIGIN, ORIGIN + DOWN * 20 + DOWN * (uniform(-0.4,0.4)), color=visuals["color_linea_hilo"])
        main.label = Text(main.nombre, color=visuals["color_label_hilo"]).next_to(main.linea, UP).scale(0.5)
        main.posicion = 0
        main.juntar()
        self.grupo.add(main.total)
        self.n_hilos += 1
        return main

    def start(self, origen, nombre):
        self.n_hilos += 1
        dest = self.dibujar_hilo(f"{nombre}")
        trigger = Rectangulo(f"start({nombre})")
        arrow = Flecha(trigger.get_right(), dest.linea.get_start())
        start = VGroup(trigger, arrow)
        control = Dot(origen.linea.get_start())
        control2 = Dot(origen.linea.get_start() + DOWN * origen.count + DOWN * (uniform(-0.4,0.4)) - trigger.get_center(), color=RED).set_z_index(4)
        start.shift(origen.linea.get_start() + DOWN * origen.count + DOWN * (uniform(-0.4,0.4)) - trigger.get_center())
        origen.add_start(start)
        self.grupo.add(start, control, control2)
        return dest

    def dibujar_hilo(self, name):
        '''Dibuja un hilo en la pantalla
        y crea un objeto hilo'''
        hilo = Hilo(name)
        hilo.posicion = RIGHT * (self.n_hilos - 1) * 2  + DOWN * (uniform(-0.4,0.4))
        hilo.linea = Line(hilo.posicion, hilo.posicion + DOWN * 20, color=visuals["color_linea_hilo"])
        hilo.label = Text(hilo.nombre, color=visuals["color_label_hilo"]).next_to(hilo.linea, UP).scale(0.5)
        hilo.juntar()
        self.grupo.add(hilo.total)
        return hilo

    def sleep(self, hilo, n):
        sleep = Rectangulo(f"sleep({n})")
        sleep.move_to(hilo.linea.get_start() + DOWN * hilo.count + DOWN * (uniform(-0.4,0.4)) - sleep.get_center())
        hilo.total.add(sleep)
        hilo.count += n


    def await_(self, hilo, destino):
        if self.show_semaf:
            num = VGroup()
            cola_label = VGroup()
            texto = Text("await").move_to(hilo.linea.get_start() + DOWN * hilo.count + DOWN * (uniform(-0.4,0.4))).scale(0.2).set_z_index(2)
            box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
            flecha = DashedLine(
                start=box.get_center(),
                end=[destino.linea.get_x(), box.get_y(), 0],
                buff=0,
                dash_length=0.1,
                stroke_width=1,
                tip_length=0.1,
                tip_style={  # Estilo personalizado de la flecha
                "color": WHITE,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
                }
            ).add_tip()
            if self.recursos > 0:
                self.recursos -= 1
                num = Text(f"{self.recursos}").move_to(flecha.get_end() + RIGHT * 1).scale(0.3).set_z_index(2)
                cola_text = ", ".join([h.nombre for h in self.cola])
                cola_label = Text(f"{cola_text}").move_to(flecha.get_end() + RIGHT * 2).scale(0.3).set_z_index(2)
            else:
                self.cola.append(hilo)
                cola_text = ", ".join([h.nombre for h in self.cola])
                cola_label = Text(f"{cola_text}").move_to(flecha.get_end() + RIGHT * 2).scale(0.3).set_z_index(2)
                num = Text(f"{self.recursos}").move_to(flecha.get_end() + RIGHT * 1).scale(0.3).set_z_index(2)
            awaite = VGroup(texto, box, flecha, num, cola_label)
            hilo.awaits.append(awaite)
            hilo.juntar()
            hilo.count += 1


    def signal(self, hilo, destino):
        if self.show_semaf:
            num = VGroup()
            cola_label = VGroup()
            texto = Text("signal").move_to(hilo.linea.get_start() + DOWN * hilo.count + DOWN * (uniform(-0.4,0.4))).scale(0.2).set_z_index(2)
            box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
            flecha = DashedLine(
                start=[destino.linea.get_x(), box.get_y(), 0],
                end=box.get_center(),
                buff=0,
                dash_length=0.1,
                stroke_width=1,
                tip_length=0.1,
                tip_style={  # Estilo personalizado de la flecha
                "color": WHITE,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
                }
            ).add_tip()
            if self.cola:
                hilo = self.cola.pop(0)
                cola_text = ", ".join([h.nombre for h in self.cola])
                cola_label = Text(f"{cola_text}").move_to(flecha.get_start() + RIGHT * 2).scale(0.3).set_z_index(2)
                num = Text(f"{self.recursos}").move_to(flecha.get_start() + RIGHT * 1).scale(0.3).set_z_index(2)
            else:
                self.recursos += 1
                num = Text(f"{self.recursos}").move_to(flecha.get_start() + RIGHT * 1).scale(0.3).set_z_index(2)
                cola_text = ", ".join([h.nombre for h in self.cola])
                cola_label = Text(f"{cola_text}").move_to(flecha.get_start() + RIGHT * 2).scale(0.3).set_z_index(2)
            signal = VGroup(texto, box, flecha, num, cola_label)
            hilo.signals.append(signal)
            hilo.juntar()
            hilo.count += 1

    '''
    def start(self, origen, destino):
        texto = Text(f"start({destino.nombre})").move_to(origen.linea.get_start() + DOWN * origen.count + DOWN * (uniform(-0.4,0.4))).scale(0.2).set_z_index(2)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
        flecha = DashedLine(
            start=box.get_center(),
            end=[destino.linea.get_x(), box.get_y(), 0],
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
            "color": WHITE,
            "stroke_width": 1,
            "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()
    
        # Agrupar elementos en un VGroup
        start = VGroup(texto, box, flecha)
        self.md.ajustarAltura(destino, box.get_y())
        origen.starts.append(start)
        origen.juntar()
        origen.count += 1
        '''

    def critic(self, hilo):    
        critic = Rectangulo(f"critic")
        critic.move_to(hilo.linea.get_start() + DOWN * hilo.count + DOWN * (uniform(-0.4,0.4)) - critic.get_center())
        hilo.total.add(critic)
        hilo.count += 1

    def join(self, origen, destino):
        join = Rectangulo(f"join({destino.nombre})")
        join.move_to(origen.linea.get_start() + DOWN * origen.count + DOWN * (uniform(-0.4,0.4)) - join.get_center())
        origen.total.add(join)
        destino.joinedby.append(origen)
        origen.count += 1
