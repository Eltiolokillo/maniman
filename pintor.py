from manim import *
import json
from random import uniform

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
config = load_config("config.json")

class Pintor:
    def __init__(self, md, show_semaf, recursos, cola):
        self.md = md
        self.show_semaf = show_semaf
        self.recursos = recursos
        self.cola = cola
        
    def dibujar_hilo(self, hilo):
        # Crear línea y etiqueta del hilo
        hilo.linea = Line(hilo.posicion, hilo.posicion + DOWN * 20 + DOWN * (uniform(-0.4,0.4)), color=config["color_linea_hilo"])
        hilo.label = Text(hilo.nombre, color=config["color_label_hilo"]).next_to(hilo.linea, UP).scale(0.5)
        hilo.juntar()

    def sleep(self, hilo, n):
        texto = Text(f"sleep({n})").move_to(hilo.linea.get_start() + DOWN * hilo.count + DOWN * (uniform(-0.4,0.4))).scale(0.2).set_z_index(2)
        box = SurroundingRectangle(texto,stroke_width=config["borde_box"],color=config["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
        sleep = VGroup(texto, box)
        hilo.sleeps.append(sleep)
        hilo.juntar()
        hilo.count += n


    def await_(self, hilo, destino):
        if self.show_semaf:
            num = VGroup()
            cola_label = VGroup()
            texto = Text("await").move_to(hilo.linea.get_start() + DOWN * hilo.count + DOWN * (uniform(-0.4,0.4))).scale(0.2).set_z_index(2)
            box = SurroundingRectangle(texto,stroke_width=config["borde_box"],color=config["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
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
            box = SurroundingRectangle(texto,stroke_width=config["borde_box"],color=config["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
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


    def start(self, origen, destino):
        texto = Text(f"start({destino.nombre})").move_to(origen.linea.get_start() + DOWN * origen.count + DOWN * (uniform(-0.4,0.4))).scale(0.2).set_z_index(2)
        box = SurroundingRectangle(texto,stroke_width=config["borde_box"],color=config["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
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


    def critic(self, hilo):    
        texto = Text("SecCritic").move_to(hilo.linea.get_start() + DOWN * hilo.count + DOWN * (uniform(-0.4,0.4))).scale(0.2).set_z_index(2)
        box = SurroundingRectangle(texto,stroke_width=config["borde_box"],color=config["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
        critic = VGroup(texto, box)
        hilo.criticas.append(critic)
        hilo.juntar()
        hilo.count += 1

    def join(self, origen, destino):
        texto = Text(f"join({destino.nombre})").move_to(origen.linea.get_start() + DOWN * origen.count + DOWN * (uniform(-0.4,0.4))).scale(0.2).set_z_index(2)
        box = SurroundingRectangle(texto,stroke_width=config["borde_box"],color=config["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
        join = VGroup(texto,box)
        origen.joins.append(join)
        destino.joinedby.append(origen)
        origen.juntar()
        origen.count += 1
