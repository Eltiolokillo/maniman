from manim import config

visuals ={
    "color_linea_main" : "WHITE",
    "color_label_main" : "WHITE",
    "color_linea_semaforo" : "WHITE",
    "color_label_semaforo" : "WHITE",
    "color_linea_hilo" : "BLUE",
    "color_label_hilo" : "WHITE",
    "color_text" : "WHITE",
    "color_box" : "WHITE",
    "borde_box" : 1,
    "color_flecha" : "WHITE",
    "green" : "#008000",
    "red" : "#FF0000",
    "color_tramo_bien": "WHITE",
    "color_tramo_bloq": "#FF0000",
    "color_tramo_sleep": "YELLOW"
}

def calidad(quality):
    config.quality = quality

def guardar_png(a_png):
    config.save_last_frame = a_png

