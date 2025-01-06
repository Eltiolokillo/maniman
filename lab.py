from manim import *

from objetosx import * 
from visuales import * 

from config import visuals

#python -m manim lab.py Escena2 --save_last_frame

config.quality = "high_quality"

HTML_GREEN = "#008000"
HTML_RED = "#FF0000"


class Test(Scene):
    def construct(self):
        t = Text("Hola Mundo").scale(2).shift(UP * 2)
        c = Circle().shift(DOWN * 2)
        s = Square().shift(LEFT * 2)
        tr = Triangle().shift(RIGHT * 2)

        d = Text("HolaMundo", )

        g = VGroup(t,c,s,tr)

        self.play(Create(g))

        self.wait(2)

        self.play(FadeOut(g))

        self.play(Create(t), Create(c), Create(s), Create(tr))

        self.wait(2)
