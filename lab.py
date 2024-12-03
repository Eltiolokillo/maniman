from manim import *

from objetos import * 

class Escenax(MovingCameraScene):
    def construct(self):
        control = Dot(ORIGIN)
        trigger = Rectangulo(f"start")
        arrow = Flecha(trigger.get_right(), trigger.get_right() + LEFT * 2)
        start = VGroup(trigger, arrow)
        start.shift([2,2,0] - trigger.get_center())
        grid = NumberPlane()

        texto = Text("CAMBIOS")

        self.play(Create(grid))

        self.play(Create(texto))

        self.play(Create(control), Create(start))
        self.wait(2)
