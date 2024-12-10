from manim import *

from objetos import * 

from config import visuals

class Escenax(MovingCameraScene):
    def construct(self):
        
        grid = NumberPlane()

        objeto = Triangle(color = visuals["color_linea_hilo"]).shift(UP)
        obgeto = Triangle(color = visuals["color_linea_hilo"]).shift(DOWN)

        self.play(Create(grid))

        self.play(Create(obgeto), Create(objeto))
        self.wait(2)
