from manim import *

class Escena(MovingCameraScene):
    def __init__(self, grupo):
        super().__init__()
        self.grupo = grupo
    
    def construct(self):
        # Renderizar animación
        #grid = NumberPlane()
        #self.play(Create(grid))

        self.play(Create(self.grupo))

        self.play(self.camera.frame.animate.set(width=self.camera.frame.width * 1.5).move_to(RIGHT * 3 + DOWN * 2))

        self.wait(2)
        
        



        

    