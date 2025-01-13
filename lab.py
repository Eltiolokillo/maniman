from manim import *

from maniman.core.visuales import * 

from maniman.config.config import visuals

#python -m manim lab.py Escena2 --save_last_frame

config.quality = "high_quality"
config.save_last_frame = True

HTML_GREEN = "#008000"
HTML_RED = "#FF0000"


class EscenaEjemploManim1(Scene):
    def construct(self):
        c = Circle().shift(UP * 2 + LEFT * 3)
        t = Text("Hola Mundo").shift(UP * 2 + RIGHT * 3)
        t1 = Text("Hola Mundo").next_to(t, DOWN).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        s = Square(side_length=2, color=YELLOW).shift(DOWN * 2 + LEFT * 3).set_fill(HTML_GREEN, opacity=1)
        tr = Triangle().shift(DOWN * 2 + RIGHT * 3).set_fill(HTML_RED, opacity=1)

        self.add(c, t, t1, s, tr)

        self.wait(2)

class Squares(Scene):
    def construct(self):
        # Crear los grupos v1, v2 y v3
        v1 = VGroup()
        sq1v1 = Square(side_length=1, color=RED).rotate(PI/4).shift(LEFT * 5.5)
        sq2v1 = Square(side_length=1, color=RED).rotate(PI/4).shift(LEFT * 3.5)
        v1.add(sq1v1, sq2v1)

        v2 = VGroup()
        sq1v2 = Square(side_length=1, color=interpolate_color(RED, GREEN, 1/5)).rotate(PI/4).shift(LEFT * 0.5)
        sq2v2 = Square(side_length=1, color=interpolate_color(RED, GREEN, 1/5)).rotate(PI/4).shift(RIGHT * 0.5)
        v2.add(sq1v2, sq2v2)

        v3 = VGroup()
        sq1v3 = Square(side_length=1, color=GREEN).rotate(PI/4).shift(RIGHT * 3.5)
        sq2v3 = Square(side_length=1, color=GREEN).rotate(PI/4).shift(RIGHT * 4)
        v3.add(sq1v3, sq2v3)

        # Crear cuadrados grandes alrededor de cada grupo sin rotación
        border1 = Rectangle(width=4, height=3).shift(LEFT * 4.5)
        border2 = Rectangle(width=4, height=3).shift(ORIGIN)
        border3 = Rectangle(width=4, height=3).shift(RIGHT * 4.5)

        # Asegurarse que los grupos estén centrados respecto a sus fronteras
        v1.move_to(border1.get_center())
        v2.move_to(border2.get_center())
        v3.move_to(border3.get_center())

        # Añadir los grupos y los bordes a la escena
        self.add(border1, v1, border2, v2, border3, v3)

class ElementosDiagrama(Scene):
    def construct(self):
        i1 = VGroup()
        hilo = Line(start=UP*2 + LEFT*3, end=DOWN*2 + LEFT*3, color=WHITE).scale(0.5)
        label = Text("main").next_to(hilo, UP).set_color(WHITE).scale(0.3)
        caption1 = Text("Hilo").set_color(YELLOW).scale(0.5)

        caption1.shift(DOWN*2 + LEFT*4.5)

        i1.add(hilo, label)
        i1.next_to(caption1, UP)

        i2 = VGroup()
        accion = Text("start(a)").scale(0.3)
        caja = SurroundingRectangle(accion, color=WHITE)
        caption2 = Text("Accion").set_color(YELLOW).scale(0.5)

        caption2.shift(DOWN*2 + LEFT*1.5)

        i2.add(accion, caja)
        i2.next_to(caption2, UP).shift(UP*1)

        i3 = VGroup()
        flecha = DashedLine(start=UP*2 + RIGHT*2, end=UP*2 + RIGHT*3, color=WHITE).add_tip()
        caption3 = Text("Flecha").set_color(YELLOW).scale(0.5)

        caption3.shift(DOWN*2 + RIGHT*1.5)

        i3.add(flecha)
        i3.next_to(caption3, UP).shift(UP*1)
        
        i4 = VGroup()
        fLine = Line(start=UP*2 + RIGHT*2.5, end=DOWN*2 + RIGHT*2.5, color=WHITE).scale(0.5)
        fLabel = Text("main").next_to(fLine, UP).set_color(WHITE).scale(0.3)
        fAccion = Text("start(a)").scale(0.3).move_to(fLabel.get_center() + DOWN*1).set_z_index(2)
        fCaja = SurroundingRectangle(fAccion, color=WHITE).set_z_index(1).set_fill(BLACK, opacity=1)
        fFlecha = DashedLine(start=fCaja.get_right(), end=fCaja.get_right() + RIGHT *1, color=WHITE).add_tip()
        caption4 = Text("Ejemplo").set_color(YELLOW).scale(0.5)

        caption4.shift(DOWN*2 + RIGHT*4.5)

        i4.add(fLine, fLabel, fAccion, fCaja, fFlecha)
        i4.next_to(caption4, UP)

        self.add(caption1, caption2, caption3, caption4)

        self.add(i1, i2, i3, i4)