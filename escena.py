from manim import *

class Escena(MovingCameraScene):
    def __init__(self):
        super().__init__()
        self.n_hilos = 0
        self.n_semaforos = 0

    def construct(self):
        # Renderizar animación
        #grid = NumberPlane()
        #self.play(Create(grid))

        self.play(Create(self.grupo))

        self.play(self.camera.frame.animate.set(width=self.camera.frame.width * 1.5).move_to(RIGHT * 3 + DOWN * 2))

        self.wait(2)
        
        



        

    