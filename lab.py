from manim import *

from objetos import * 

from config import visuals

config.save_last_frame = True
config.quality = "high_quality"

HTML_GREEN = "#008000"
HTML_RED = "#FF0000"

class Escenax(MovingCameraScene):
    def construct(self):
        
        grid = NumberPlane()

        self.play(Create(grid))



class Escena1(MovingCameraScene):
    def construct(self):
        def top_left(pos):
            return pos + LEFT * 8 + UP * 4

        # MAIN
        main = Line(start=top_left(ORIGIN),end=top_left(ORIGIN + DOWN*20),color=WHITE)
        main_label = Text("main").next_to(main, UP).scale(0.5)

        texto = Text("start(a)").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        startA = VGroup(box, texto).move_to(top_left([0, -1, 0]))

        texto = Text("join(a)").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        joinA = VGroup(box, texto).move_to(top_left([0,-2,0]))

        texto = Text("start(c)").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        startC = VGroup(box, texto).move_to(top_left([0,-7.5,0]))

        texto = Text("join(c)").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        joinC = VGroup(box, texto).move_to(top_left([0,-9.5,0]))

        main_bloq1 = Line(start=joinA.get_bottom(), end=top_left([0,-6.5,0]), color=HTML_RED)
        main_bloq2 = Line(start=joinC.get_bottom(), end=top_left([0,-10,0]), color=HTML_RED)

        # A
        a = Line(start=top_left([3,-1,0]),end=top_left([3,-6.5,0]),color=WHITE)
        a_label = Text("a").next_to(a, UP).scale(0.5)

        texto = Text("await").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        a_await = VGroup(box, texto).move_to(top_left([3,-2,0]))

        texto = Text("crit").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        a_crit = VGroup(box, texto).move_to(top_left([3,-2.5,0]))

        texto = Text("start(b)").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        a_start_b = VGroup(box, texto).move_to(top_left([3,-3.5,0]))

        texto = Text("signal").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        a_signal = VGroup(box,texto).move_to(top_left([3,-4.5,0]))

        texto = Text("join(b)").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        a_join_b = VGroup(box,texto).move_to(top_left([3,-5.5,0]))

        a_bloq = Line(start=top_left([3,-5.5,0]), end=top_left([3,-6.5,0]), color=HTML_RED)

        # B
        b = Line(start=top_left([6,-3.5,0]),end=top_left([6,-6.5,0]),color=WHITE)
        b_label = Text("b").next_to(b, UP).scale(0.5)

        texto = Text("crit").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        b_crit = VGroup(box, texto).move_to(top_left([6,-4,0]))

        # C
        c = Line(start=top_left([9,-7.5,0]),end=top_left([9,-10,0]),color=WHITE)
        c_label = Text("c").next_to(c, UP).scale(0.5)

        texto = Text("sleep").scale(0.3)
        box = SurroundingRectangle(texto,stroke_width=visuals["borde_box"],color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        c_sleep = VGroup(box, texto).move_to(top_left([9,-8,0]))

        # Semaforo
        semaforo = Line(start=top_left([12,0,0]), end=top_left([12,0,0]+ DOWN*20))
        semaforo_label = Text("sem").next_to(semaforo, UP).scale(0.5)

        texto = Text("1").scale(0.5)
        circle = Circle(color=WHITE).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_inicio = VGroup(circle, texto).next_to(semaforo_label, RIGHT)

        texto = Text("0").scale(0.5)
        circle = Circle(color=HTML_RED).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_wait_a = VGroup(circle, texto).move_to(top_left([12,-2,0]))

        texto = Text("1").scale(0.5)
        circle = Circle(color=HTML_GREEN).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_signal_a = VGroup(circle, texto).move_to(top_left([12,-4.5,0]))

        sem_bloq = Line(start=top_left([12,-2,0]), end=top_left([12,-4.5,0]), color=HTML_RED)

        # Flechas

        fl_m_a = DashedLine(
            start=startA.get_right(),
            end=a.get_start(),
            buff=0, dash_length=0.1, stroke_width=1, tip_length=0.1, 
            tip_style={
                "color": WHITE,
                "stroke_width": 1,
                "fill_opacity": 0,
                }
        ).add_tip()


        fl_wa_s = DashedLine(
            start=a_await.get_right(),
            end=sem_wait_a.get_left(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
            "color": HTML_RED,
            "stroke_width": 1,
            "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_a_b = DashedLine(
            start=a_start_b.get_right(),
            end=b.get_start(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
            "color": WHITE,
            "stroke_width": 1,
            "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_sa_s = DashedLine(
            start=a_signal.get_right(),
            end=sem_signal_a.get_left(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
            "color": HTML_GREEN,
            "stroke_width": 1,
            "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_b_a = DashedLine(
            start=b.get_end(),
            end=a.get_end(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
            "color": HTML_GREEN,
            "stroke_width": 1,
            "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_a_m = DashedLine(
            start=a.get_end(),
            end=main_bloq1.get_end(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
            "color": WHITE,
            "stroke_width": 1,
            "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_m_c = DashedLine(
            start=startC.get_right(),
            end=c.get_start(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
            "color": WHITE,
            "stroke_width": 1,
            "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_c_m = DashedLine(
            start=c.get_end(),
            end=main_bloq2.get_end(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
            "color": WHITE,
            "stroke_width": 1,
            "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()


        self.camera.frame.scale(2)

        self.add(fl_m_a, fl_wa_s, fl_a_b, fl_sa_s, fl_b_a, fl_a_m, fl_m_c, fl_c_m)

        # Elementos de main
        self.add(main, main_bloq1, main_bloq2, main_label, startA, joinA, startC, joinC)

        # Elementos de a
        self.add(a, a_label, a_bloq, a_await, a_crit, a_start_b, a_signal, a_join_b)

        # Elementos de b
        self.add(b, b_label, b_crit)

        # Elementos de c
        self.add(c, c_label, c_sleep)

        # Elementos de semaforo
        self.add(semaforo, semaforo_label, sem_bloq, sem_inicio, sem_wait_a, sem_signal_a)

        self.wait(2)


class Escena2(MovingCameraScene):
    def construct(self):
        def top_left(pos):
            return pos + LEFT * 8 + UP * 4

        # MAIN
        main = Line(start=top_left(ORIGIN), end=top_left(ORIGIN + DOWN * 20), color=WHITE)
        main_label = Text("main").next_to(main, UP).scale(0.5)

        texto = Text("start(a)").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        startA = VGroup(box, texto).move_to(top_left([0, -1, 0]))

        texto = Text("start(b)").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        startB = VGroup(box, texto).move_to(top_left([0, -2, 0]))

        texto = Text("start(c)").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        startC = VGroup(box, texto).move_to(top_left([0, -3, 0]))

        texto = Text("start(d)").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        startD = VGroup(box, texto).move_to(top_left([0, -4, 0]))

        texto = Text("join(a)").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        joinA = VGroup(box, texto).move_to(top_left([0, -5, 0]))

        texto = Text("join(b)").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        joinB = VGroup(box, texto).move_to(top_left([0, -6.5, 0]))

        texto = Text("join(c)").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        joinC = VGroup(box, texto).move_to(top_left([0, -8, 0]))

        texto = Text("join(d)").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        joinD = VGroup(box, texto).move_to(top_left([0, -9, 0]))

        main_bloqa = Line(start=joinA.get_bottom(), end=top_left([0, -6, 0]), color=HTML_RED)

        main_bloqb = Line(start=joinB.get_bottom(), end=top_left([0, -7.5, 0]), color=HTML_RED)

        main_bloqd =  Line(start=joinD.get_bottom(), end=main.get_end(), color=HTML_RED)

        # A
        a = Line(start=top_left([3, -1, 0]), end=top_left([3, -6, 0]), color=WHITE)
        a_label = Text("a").next_to(a, UP).scale(0.5)

        texto = Text("await").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        a_await = VGroup(box, texto).move_to(top_left([3, -1.5, 0]))

        texto = Text("sleep").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        a_sleep = VGroup(box, texto).move_to(top_left([3, -2, 0]))

        texto = Text("signal").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        a_signal = VGroup(box, texto).move_to(top_left([3, -4.5, 0]))

        # B
        b = Line(start=top_left([6, -2, 0]), end=top_left([6, -7.5, 0]), color=WHITE)
        b_label = Text("b").next_to(b, UP).scale(0.5)

        texto = Text("sleep").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        b_sleep = VGroup(box, texto).move_to(top_left([6, -2.5, 0]))

        texto = Text("await").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        b_await = VGroup(box, texto).move_to(top_left([6, -5.5, 0]))

        b_bloq = Line(start=b_await.get_bottom(), end=b.get_end(), color=HTML_RED)

        # C
        c = Line(start=top_left([9, -3, 0]), end=top_left([9, -7.5, 0]), color=WHITE)
        c_label = Text("c").next_to(c, UP).scale(0.5)

        texto = Text("await").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        c_await = VGroup(box, texto).move_to(top_left([9, -3.5, 0]))

        texto = Text("crit").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        c_crit = VGroup(box, texto).move_to(top_left([9, -5, 0]))

        texto = Text("signal").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        c_signal = VGroup(box, texto).move_to(top_left([9, -7, 0]))

        c_bloq = Line(start=c_await.get_bottom(), end=c_crit.get_top(), color=HTML_RED)

        # D
        d = Line(start=top_left([12, -4, 0]), end=top_left([12, -20, 0]), color=WHITE)
        d_label = Text("d").next_to(d, UP).scale(0.5)

        texto = Text("await").scale(0.3)
        box = SurroundingRectangle(texto, stroke_width=visuals["borde_box"], color=visuals["color_box"]).set_fill(BLACK, opacity=1)
        d_await = VGroup(box, texto).move_to(top_left([12, -6, 0]))

        d_bloq = Line(start=d_await.get_bottom(), end=d.get_end(), color=HTML_RED)

        # Semaforo
        semaforo = Line(start=top_left([15, 0, 0]), end=top_left([15, 0, 0] + DOWN * 20), color=WHITE)
        semaforo_label = Text("sem").next_to(semaforo, UP).scale(0.5)

        texto = Text("1").scale(0.5)
        circle = Circle(color=WHITE).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_inicio = VGroup(circle, texto).next_to(semaforo_label, RIGHT)

        texto = Text("0").scale(0.5)
        circle = Circle(color=HTML_RED).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_wait_a = VGroup(circle, texto).move_to(top_left([15, -1.5, 0]))

        texto = Text("0").scale(0.5)
        circle = Circle(color=HTML_RED).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_wait_c = VGroup(circle, texto).move_to(top_left([15,-3.5, 0]))

        sem_cola_c1 = Text("c", disable_ligatures=True, color=HTML_RED).scale(0.5).next_to(sem_wait_c, RIGHT)

        texto = Text("0").scale(0.5)
        circle = Circle(color=HTML_RED).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_signal_a = VGroup(circle, texto).move_to(top_left([15, -4.5, 0]))

        sem_cola_c2 = Text("c", disable_ligatures=True, color=HTML_GREEN).scale(0.5).next_to(sem_signal_a, RIGHT)

        texto = Text("0").scale(0.5)
        circle = Circle(color=HTML_RED).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_wait_b = VGroup(circle, texto).move_to(top_left([15, -5.5, 0]))

        sem_cola_b = Text("b",disable_ligatures=True, color=HTML_RED).scale(0.5).next_to(sem_wait_b, RIGHT)

        texto = Text("0").scale(0.5)
        circle = Circle(color=HTML_RED).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_wait_d = VGroup(circle, texto).move_to(top_left([15, -6, 0]))

        sem_cola_bd = MarkupText('<span color="red">b</span>   <span color="red">d</span>').scale(0.5).next_to(sem_wait_d, RIGHT)

        texto = Text("0").scale(0.5)
        circle = Circle(color=HTML_RED).move_to(texto.get_center_of_mass()).set_fill(BLACK, opacity=1).scale(0.4)
        sem_signal_c = VGroup(circle, texto).move_to(top_left([15, -7, 0]))
        
        sem_cola_d = MarkupText('<span color="green">b</span>   <span color="red">d</span>').scale(0.5).next_to(sem_signal_c, RIGHT)

        sem_bloq_a = Line(start=top_left([15, -1.5, 0]), end=semaforo.get_end(), color=WHITE)


        # Flechas
        fl_m_a = DashedLine(
            start=startA.get_right(),
            end=a.get_start(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
                "color": WHITE,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_m_b = DashedLine(
            start=startB.get_right(),
            end=b.get_start(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
                "color": WHITE,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_m_c = DashedLine(
            start=startC.get_right(),
            end=c.get_start(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
                "color": WHITE,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_m_d = DashedLine(
            start=startD.get_right(),
            end=d.get_start(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            tip_style={  # Estilo personalizado de la flecha
                "color": WHITE,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_wa_s = DashedLine(
            start=a_await.get_right(),
            end=sem_wait_a.get_left(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_RED,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_RED,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_wb_s = DashedLine(
            start=b_await.get_right(),
            end=sem_wait_b.get_left(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_RED,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_RED,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_wc_s = DashedLine(
            start=c_await.get_right(),
            end=sem_wait_c.get_left(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_RED,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_RED,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_wd_s = DashedLine(
            start=d_await.get_right(),
            end=sem_wait_d.get_left(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_RED,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_RED,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()
        
        fl_sa_s = DashedLine(
            start=a_signal.get_right(),
            end=sem_cola_c2.get_left(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_GREEN,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_GREEN,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_lc = DashedLine(
            start = sem_cola_c2.get_left(),
            end = c_crit.get_top(),
            buff = 0,
            dash_length = 0.1,
            stroke_width = 1,
            tip_length = 0.1,
            color = HTML_GREEN,
            tip_style = {
                "color": HTML_GREEN,
                "stroke_width": 1,
                "fill_opacity": 0,
            }
        ).add_tip()

        fl_sc_s = DashedLine(
            start=c_signal.get_right(),
            end=sem_cola_d.get_left(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_GREEN,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_GREEN,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_lb = DashedLine(
            start=sem_cola_d.get_left(),
            end=b.get_end(),
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_GREEN,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_RED,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_a_m = DashedLine(
            start=a.get_end(),
            end=[main.get_start()[0], a.get_end()[1], 0],
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_GREEN,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_GREEN,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()
        
        fl_b_m = DashedLine(
            start=b.get_end(),
            end=[main.get_start()[0], b.get_end()[1], 0],
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_GREEN,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_GREEN,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()

        fl_c_m = DashedLine(
            start=c.get_end(),
            end=[main.get_start()[0], c.get_end()[1], 0],
            buff=0,
            dash_length=0.1,
            stroke_width=1,
            tip_length=0.1,
            color=HTML_GREEN,
            tip_style={  # Estilo personalizado de la flecha
                "color": HTML_GREEN,
                "stroke_width": 1,
                "fill_opacity": 0,  # Quitar relleno
            }
        ).add_tip()



        # Agregar elementos a la escena
        self.camera.frame.scale(2)

        self.add(fl_m_a, fl_m_b, fl_m_c, fl_m_d)
        self.add(fl_wa_s, fl_wb_s, fl_wc_s, fl_wd_s)
        self.add(fl_sa_s, fl_sc_s, fl_lc, fl_lb)
        self.add(fl_a_m, fl_b_m, fl_c_m)
        self.add(main, main_label, main_bloqa, main_bloqb, main_bloqd, startA, startB, startC, startD, joinA, joinB, joinC, joinD)
        self.add(a, a_label, a_await, a_sleep, a_signal)
        self.add(b, b_label, b_bloq, b_sleep, b_await)
        self.add(c, c_label, c_bloq, c_await, c_crit, c_signal)
        self.add(d, d_label, d_bloq, d_await)
        self.add(semaforo, semaforo_label, sem_bloq_a, sem_inicio, sem_wait_a, sem_wait_c, sem_signal_a, sem_wait_b, sem_wait_d, sem_signal_c)
        self.add(sem_cola_c1, sem_cola_c2, sem_cola_b, sem_cola_bd, sem_cola_d)

        self.wait(2)







