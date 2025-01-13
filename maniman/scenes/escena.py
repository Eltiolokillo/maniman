from manim import *

from maniman.core.diagrama import *

config.save_last_frame = True
config.quality = "high_quality"

class Escena(MovingCameraScene):
    def __init__(self, g):
        super().__init__()
        self.g = g
        

    def construct(self):
        
        
        x_min = float('inf')
        x_max = float('-inf')


        for grupo in self.g:
            for elem in grupo:
                left_x = elem.get_left()[0]
                right_x = elem.get_right()[0]
                x_min = min(x_min, left_x)
                x_max = max(x_max, right_x)
                self.todoJunto.add(elem)

        x_center = (x_min + x_max) / 2.0


        self.camera.frame.set(width=self.camera.frame.width * 1.5).move_to(DOWN*4)

        current_center = self.camera.frame.get_center()
        new_center = [x_center, current_center[1], current_center[2]]

        self.play(self.camera.frame.animate.move_to(new_center))

        for grupo in self.g:
            # Construye una lista de animaciones Create(...) para cada elemento
            anims = [Create(elem) for elem in grupo]
            # Pásalas "desempaquetadas" a self.play()
            self.play(*anims)
            self.wait(1)

        self.wait(2)

        
        



        

    