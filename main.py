from maniman import *

def main():
    d1 = Diagrama()
    main = d1.new_thread("main")
    a = d1.start(main, "x")
    b = d1.start(main, "y")
    
    d1.accion(a, "hola")
    d1.sleep(a, 2)
    c = d1.start(a, "c")

    d1.sleep(b, 3)

    d1.sleep(c, 3)

    calidad("low_quality")
    guardar_png(True)

    d1.crear_escena()
    

if __name__ == "__main__":
    main()

