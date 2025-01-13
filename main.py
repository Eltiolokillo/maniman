from maniman import *

def main():
    d1 = Diagrama()
    main = d1.new_thread("main")
    a = d1.start(main, "a")
    s1 = d1.new_semaphore("s1", 1)
    b = d1.start(main, "b")
    c = d1.start(main, "c")
    d1.join(main,a)
    d1.sleep(main, 2)
    d1.join(main,b)
    d1.join(main,c)

    
            
    d1.await_(a, s1)
    d1.sleep(a, 3)
    d1.signal(a, s1)
    d1.end(a)

    d1.await_(b, s1)
    d1.unaria(b, "seccionCritica")
    d1.end(b)

    d1.await_(c, s1)
    d1.sleep(c, 2)
    d1.signal(c,s1)
    d1.end(c)

    d1.crear_escena()
    

if __name__ == "__main__":
    main()

