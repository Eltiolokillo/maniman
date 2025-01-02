from manim import *

from objetosx import * 
from visuales import * 

from config import visuals

#python -m manim lab.py Escena2 --save_last_frame

config.save_last_frame = True
config.quality = "high_quality"

HTML_GREEN = "#008000"
HTML_RED = "#FF0000"

class Escenax(MovingCameraScene):
    def construct(self):
        
        grid = NumberPlane()
        t1 = Text("Primero").shift(LEFT * 2)
        t2 = Text("Primero").shift(RIGHT * 2)

        visuales_accion(t2)

        self.play(Create(grid))
        self.play(Create(t1), Create(t2))
        self.wait(2)


class ArrowScene(Scene):
    def construct(self):
        # Crear una flecha larga
        long_arrow = DashedLine(
            start=[-4, 0, 0],
            end=[4, 0, 0],
            buff=0,
            stroke_width=1,
            dash_length=0.3,
            dashed_ratio=0.5,
            tip_length=0.2,
            tip_style={  
                "color": RED,
                "stroke_width": 1,
                "fill_opacity": 0,  
            }
        ).add_tip()

        # Crear una flecha corta
        short_arrow = DashedLine(
            start=[-2, -2, 0],
            end=[2, -2, 0],
            buff=0,
            stroke_width=1,
            dash_length=0.3,
            dashed_ratio=0.5,
            tip_length=0.2,
            tip_style={  
                "color": BLUE,
                "stroke_width": 1,
                "fill_opacity": 0,  
            }
        ).add_tip()

        # Añadir las flechas a la escena
        self.add(long_arrow, short_arrow)