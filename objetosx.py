from manim import *

from config import visuals

class Elemento(VGroup):
    def __init__(self):
        super().__init__()
        self.t = 0

class Rectangulo(Elemento):
    def __init__(self, name):
        super().__init__()
        texto = Text(name).scale(0.2).set_z_index(2)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)
        self.add(texto, box)
    
    
class Flecha(Elemento):
    def __init__(self, s, e):
        super().__init__()
        flecha = DashedLine(
                start=s,
                end=e,
                buff=0,
                dash_length=0.1,
                stroke_width=1,
                tip_length=0.1,
                tip_style={  
                "color": visuals["color_flecha"],
                "stroke_width": 1,
                "fill_opacity": 0,  
                }
            ).add_tip()
        self.add(flecha)