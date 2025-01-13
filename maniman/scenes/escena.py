from manim import *

from maniman.core.diagrama import *
from maniman.config.config import *

class Escena(MovingCameraScene):
    def __init__(self, g):
        super().__init__()
        self.g = g
        self.flags = {}

    def construct(self):
        
        self.centrar_camara()

        self.animar()


    def centrar_camara(self):
        x_min = float('inf')
        x_max = float('-inf')

        todoJunto = VGroup()

        for grupo in self.g:
            for elem in grupo:
                left_x = elem.get_left()[0]
                right_x = elem.get_right()[0]
                x_min = min(x_min, left_x)
                x_max = max(x_max, right_x)
                todoJunto.add(elem)

        x_center = (x_min + x_max) / 2.0

        self.camera.frame.set(width=self.camera.frame.width * 1.5).move_to(DOWN*4)

        current_center = self.camera.frame.get_center()
        new_center = [x_center, current_center[1], current_center[2]]

        self.play(self.camera.frame.animate.move_to(new_center))

    def animar(self):
        for grupo in self.g:
            # Construye una lista de animaciones Create(...) para cada elemento
            anims = [Create(elem) for elem in grupo]
            # Pásalas "desempaquetadas" a self.play()
            self.play(*anims)
            self.wait(1)

        self.wait(2)
