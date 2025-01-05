from manim import *

from config import visuals

def visuales_nombres(nom):
    nom.scale(0.5).set_z_index(2)

def visuales_accion(accion):
    accion.scale(0.2).set_z_index(2)

def visuales_caja_accion(caja):
    caja.set_stroke(width=visuals["borde_box"],color=visuals["color_box"]).set_z_index(1).set_fill(BLACK, opacity=1)

def crear_flecha(s,e,color=None):
    c = None
    match color:
        case "g", "green", "G", "GREEN", "Green", "verde", "VERDE", "Verde":
            c = visuals["green"]
        case "r", "red", "R", "RED", "Red", "rojo", "ROJO", "Rojo":
            c = visuals["red"]
        case _:
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
        tip_style={  
            "color": c,
            "stroke_width": 1,
            "fill_opacity": 0,  
        }
    ).add_tip()

    #f = DashedVMobject(f, dashed_ratio=0.5)

    return f

def visuales_flecha(flecha, color=None):
    c = None
    match color:
        case "g", "green", "G", "GREEN", "Green", "verde", "VERDE", "Verde":
            c = visuals["green"]
        case "r", "red", "R", "RED", "Red", "rojo", "ROJO", "Rojo":
            c = visuals["red"]
        case _:
            c = visuals["color_flecha"]
    flecha.buff(0).dash_length(0.1).stroke_width(1).tip_length(0.1).tip_style={  
                "color": c,
                "stroke_width": 1,
                "fill_opacity": 0,  
                }.add_tip()

