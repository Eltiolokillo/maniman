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

        x_min = float('inf')
        x_max = float('-inf')

        todoJunto = VGroup()

        for grupo in g:
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

        for grupo in g:
            # Construye una lista de animaciones Create(...) para cada elemento
            anims = [Create(elem) for elem in grupo]
            # Pásalas "desempaquetadas" a self.play()
            self.play(*anims)
            self.wait(1)

        self.wait(2)
        
        



        

    