from manim import *

from maniman.config.config import visuals

def visuales_nombres(nom):
    nom.scale(0.5).set_z_index(2)

def visuales_accion(accion):
    accion.scale(0.2).set_z_index(2)

def visuales_caja_accion(caja):
    caja.set_stroke(width=visuals["borde_box"],color=visuals["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)

def crear_flecha(s,e,col=None):
    if col:
        c = col
    else:
        c = visuals["color_flecha"]

    f = DashedLine(
        start=s,
        end=e,
        buff=0,
        stroke_color=c,
        stroke_width=1,
        dash_length=0.1,
        dashed_ratio=0.5,
        tip_length=0.1,
    ).add_tip(tip_length=0.1, 
              tip_shape=ArrowTriangleFilledTip)

    return f
    
def visuales_circulo(circulo):
    circulo.set_fill(BLACK, opacity=1).scale(0.4).set_z_index(1)

