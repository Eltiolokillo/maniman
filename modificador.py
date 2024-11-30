from manim import *
from random import uniform

class Modificador:
    def end(self, hilo):
        nueva_altura = hilo.count * DOWN
        hilo.linea.put_start_and_end_on(hilo.linea.get_start(), hilo.linea.get_start() + nueva_altura)

        for origen in hilo.joinedby:
            flecha = DashedLine(
                start=hilo.linea.get_end(),
                end=[origen.linea.get_x(), hilo.linea.get_end()[1], 0],
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
            hilo.total.add(flecha)

    def ajustarAltura(self, hilo, altura):
        desplazamiento = altura - hilo.posicion[1]
    
        hilo.total.shift(UP * desplazamiento)
    
        hilo.posicion[1] = altura


    def agitar(self, hilos, rango=(-0.4, 0.4)):
        """
        Ajusta las alturas de todas las acciones de todos los hilos aleatoriamente.

        Args:
            hilos (list[Hilo]): Lista de hilos a modificar.
            rango (tuple): Rango de valores (min, max) para el desplazamiento aleatorio en unidades de Manim.
        """
        desplazamientos = {}

        # Desplazar cada hilo y sus acciones como bloques independientes
        for hilo in hilos:
            # Generar desplazamiento para la línea y la etiqueta del hilo
            desplazamientos[hilo] = uniform(*rango)
            hilo.linea.shift(UP * desplazamientos[hilo])
            hilo.label.shift(UP * desplazamientos[hilo])
            hilo.posicion += UP * desplazamientos[hilo]

            # Desplazar cada acción individualmente
            for accion in hilo.total:
                if isinstance(accion, VGroup):
                    # Generar desplazamiento único para este bloque
                    desplazamiento_bloque = uniform(*rango)
                    desplazamientos[accion] = desplazamiento_bloque
                    accion.shift(UP * desplazamiento_bloque)

            # Alinear uniones (como flechas) entre hilos
            for origen in hilo.joinedby:
                if origen in desplazamientos:
                    # Calcular desplazamiento relativo para las flechas
                    desplazamiento_relativo = desplazamientos[origen] - desplazamientos[hilo]
                    for join_accion in hilo.joins:
                        if isinstance(join_accion, VGroup):
                            join_accion.shift(UP * desplazamiento_relativo)