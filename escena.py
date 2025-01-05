from manim import *

from diagrama import *

class Escena(MovingCameraScene):
    #def __init__(self):
    #    super().__init__()
        

    def construct(self):
        #self.play(Create(NumberPlane()))
        d1 = Diagrama()
        main = d1.new_thread("main")
        a = d1.start(main, "a")
        s1 = d1.new_semaphore("s1", 1)
        b = d1.start(main, "b")
        d1.join(main,a)
        d1.sleep(main, 2)
        d1.join(main,b)
        d1.accion(main, "final")
            
        d1.await_(a, s1)
        d1.sleep(a,3)
        d1.signal(a, s1)
        d1.end(a)

        d1.await_(b, s1)
        d1.signal(b,s1)
        d1.end(b)

        d1.procesar()

        d1.print_acciones()

        g = d1.a_manim()

        self.play(self.camera.frame.animate.set(width=self.camera.frame.width * 1.5).move_to(RIGHT * 3 + DOWN * 2))

        for grupo in g:
            self.play(Create(grupo))
            self.wait(1)

        self.wait(2)
        
        



        

    