from manim import *

from diagrama import *

config.save_last_frame = True

class Escena(MovingCameraScene):
    #def __init__(self):
    #    super().__init__()
    todoJunto = VGroup()

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

        #d1.procesar()

        #d1.print_acciones()

        #g = d1.a_manim()

        d2 = Diagrama()
        main = d2.new_thread("main")
        s1 = d2.new_semaphore("s1", 1)
        s2 = d2.new_semaphore("s2", 1)
        a = d2.start(main, "a")
        d2.await_(main, s1)
        b = d2.start(main, "b")
        d2.await_(a, s1)
        d2.await_(b, s1)
        d2.signal(main, s1)
        d2.join(main, a)
        d2.sleep(main, 2)
        d2.join(main, b)

        d2.await_(a, s2)
        d2.sleep(a, 3)
        d2.signal(a, s1)
        d2.signal(b, s1)
        d2.await_(b, s2)
        d2.signal(b, s2)
        d2.end(a)
        d2.end(b)
        d2.procesar()
        f = d2.a_manim()
        
        self.montar_escena(f)
    
    def montar_escena(self, g):
        x_min = float('inf')
        x_max = float('-inf')


        for grupo in g:
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

        for grupo in g:
            # Construye una lista de animaciones Create(...) para cada elemento
            anims = [Create(elem) for elem in grupo]
            # Pásalas "desempaquetadas" a self.play()
            self.play(*anims)
            self.wait(1)

        self.wait(2)

        
        



        

    