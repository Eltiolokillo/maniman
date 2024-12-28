from manim import *

from objetosx import * 

from config import visuals

#python -m manim lab.py Escena2 --save_last_frame

config.save_last_frame = True
config.quality = "high_quality"

HTML_GREEN = "#008000"
HTML_RED = "#FF0000"

class Escenax(MovingCameraScene):
    def construct(self):
        
        grid = NumberPlane()
        circ = Square()

        self.play(Create(grid))
        self.play(Create(circ))


