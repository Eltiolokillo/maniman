from manim import *

from objetos import * 

from config import visuals

class Escenax(MovingCameraScene):
    def construct(self):
        
        grid = NumberPlane()

        self.play(Create(grid))

        self.play(Create(texto))

        self.play(Create(control), Create(start))
        self.wait(2)
