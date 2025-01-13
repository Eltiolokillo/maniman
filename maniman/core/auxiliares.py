from maniman.core.objetos import *
from maniman.core.visuales import *

def print_diagrama(diagrama):
        for hilo in diagrama.hilos:
            print(f"HILO: {hilo.nombre}\n")
            for obj in hilo.objetos:
                if isinstance(obj, Unaria):
                    print(f"Accion: t = {obj.t}")
                elif isinstance(obj, Start):
                    print(f"Start: t = {obj.t}")
                elif isinstance(obj, Sleep):
                    print(f"Sleep: t = {obj.t}")
                elif isinstance(obj, Await):
                    print(f"Await: t = {obj.t}")
                elif isinstance(obj, Signal):
                    print(f"Signal: t = {obj.t}")
                elif isinstance(obj, Join):
                    print(f"Join: t = {obj.t}")
                elif isinstance(obj, End):
                    print(f"End: t = {obj.t}")
            print("\n")

def print_acciones(diagrama):
        for accion in diagrama.acciones:
            print(f"Tipo: {type(accion).__name__}, origen: {accion.hilo.nombre}, t: {accion.t}")

def ordenar(diagrama):
        diagrama.acciones.sort(key=lambda accion: accion.t)

def procesar(diagrama):
        '''
        Se ordenan las acciones y se recorren una a una, siempre y cuando no
        estén bloqueadas. Se bloquean con awaits y joins, y se liberan con
        signals y ends. Si están bloqueadas se encolan. Al desbloquear, todas
        las acciones de la cola vuelven a la lista global pero con tiempo actualizado
        t_nuevo = t_desbloqueo + t_antiguo 
        '''
        bloqueados = []         # Lista de hilos bloqueados    
        final = []              # Lista de acciones finales
        t = 0                   # Tiempo actual
        copia = diagrama.acciones    # Copia de las acciones para no modificar la original
        # Mientras haya acciones con accion.t > t en copia
        while acciones_por_procesar(t,copia):
            procesadas = []
            for accion in copia:
                # Cada accion que se ejecuta en t
                if accion.t == t:

                    # Si la accion no esta bloqueada
                    if (
                        accion.hilo.empezado and  # El hilo debe estar en diagrama.hilos
                        not accion.hilo.acabado and  # El hilo debe estar en estado no acabado
                        accion.hilo not in bloqueados and  # El hilo no debe estar en bloqueados
                        not any(accion.hilo in semaforo.bloqueados for semaforo in diagrama.semaforos)  # El hilo no debe estar bloqueado por ningún semáforo
                    ):
                        final.append(accion)
                        #print(f"TIPO: {type(accion).__name__}, hilo: {accion.hilo.nombre}, t: {accion.t}")
                        procesadas.append(accion)

                        match accion:
                            # Start ajusta tiempos de hilo creado
                            # Cada objeto del hilo, si coincide con un objeto
                            # de copia, se le añade el tiempo de creacion
                            case Start():
                                accion.destino.empezado = True
                                accion.hilo.fin_tramo(t)
                                accion.hilo.inicio_tramo(t, 'bien')
                                accion.destino.inicio_tramo(t, 'bien')
                                for enHilo in accion.destino.objetos:
                                    for acc in copia:
                                        if acc == enHilo:
                                            acc.t += t - accion.destino.y
                            
                            # Sleep ajusta color de tramo
                            case Sleep():
                                accion.hilo.fin_tramo(t)
                                accion.hilo.inicio_tramo(t, 'sleep')

                            # Hilo que llama await consume recurso. Si no hay recursos,
                            # Se bloquea
                            case Await():
                                if accion.semaforo.recursos > 0:
                                    accion.hilo.fin_tramo(t)
                                    accion.hilo.inicio_tramo(t, 'bien')
                                    accion.semaforo.cambiar_semaforo(accion.semaforo.recursos - 1, t, accion)
                                    accion.semaforo.recursos -= 1
                                    accion.recurso_final = accion.semaforo.recursos
                                    accion.cola_final = accion.semaforo.bloqueados[:]
                                else:
                                    accion.hilo.bloqueado_desde = t
                                    accion.semaforo.bloqueados.append(accion.hilo)
                                    accion.hilo.fin_tramo(t)
                                    accion.hilo.inicio_tramo(t,'bloq')
                                    accion.cola_final = accion.semaforo.bloqueados[:]
                                    accion.recurso_final = accion.semaforo.recursos
                            
                            # Si hay bloqueados, libera uno. Si no incrementa
                            # Recursos de semaforo      
                            case Signal():
                                accion.hilo.fin_tramo(t)
                                accion.hilo.inicio_tramo(t, 'bien')
                                if accion.semaforo.bloqueados:
                                    d = accion.semaforo.bloqueados.pop(0)
                                    desbloquear_sem(d, copia, t)
                                    accion.cola_final = accion.semaforo.bloqueados[:]
                                    accion.recurso_final = accion.semaforo.recursos
                                    accion.desbloquea_a = d
                                else:
                                    accion.semaforo.cambiar_semaforo(accion.semaforo.recursos + 1, t, accion)
                                    accion.semaforo.recursos += 1
                                    accion.recurso_final = accion.semaforo.recursos
                                    accion.cola_final = accion.semaforo.bloqueados[:]

                            # Hilo que hace Join se bloquea a menos que ya haya habido
                            # un end. Recorre los joinedby del hilo que hace join
                            case Join():
                                if not accion.destino.acabado:
                                    accion.hilo.bloqueado_desde = t
                                    bloqueados.append(accion.hilo)
                                    accion.hilo.fin_tramo(t)
                                    accion.hilo.inicio_tramo(t,'bloq')
                                else:
                                    accion.hilo.fin_tramo(t)
                                    accion.hilo.inicio_tramo(t, 'bien')

                            # Pone estado de hilo a acabado, y libera hilos que estan esperando
                            case End():
                                accion.hilo.acabado = True
                                accion.hilo.fin_tramo(t)
                                for esperando in accion.hilo.joinedby:
                                    desbloquear(esperando, bloqueados, copia, t)

                            case _:
                                accion.hilo.fin_tramo(t)
                                accion.hilo.inicio_tramo(t, 'bien')
            copia = [accion for accion in copia if accion not in procesadas]
            t += 1
        #print("TRAMOS:")
        #for h in diagrama.hilos:
        #    h.imprimir_tramos()
        #print("Semaforo")
        #for s in diagrama.semaforos:
        #    s.imprimir_tramos()
            
        diagrama.acciones = final
        ordenar(diagrama)

def acciones_por_procesar(t, acciones):
    return any(accion.t >= t for accion in acciones)
    
def desbloquear(hilo, lista, copia, t):
    if hilo in lista:
        for accion in (acc for acc in copia if acc.hilo == hilo):
            accion.t += t - hilo.bloqueado_desde
        lista.remove(hilo)
        hilo.fin_tramo(t)
        hilo.inicio_tramo(t,'bien')

def desbloquear_sem(hilo, copia, t):
    for accion in (acc for acc in copia if acc.hilo == hilo):
            accion.t += t - hilo.bloqueado_desde
    hilo.fin_tramo(t)
    hilo.inicio_tramo(t,'bien')

def agregar_tramos(diagrama):
    max_t = max(accion.t for accion in diagrama.acciones) + 1

    diagrama.elementos = diagrama.acciones[:]

    for h in diagrama.hilos:
        for tramo in h.tramos:
            tramo.hilo = h

            if tramo.final is not None:
                    
                start = tramo.t
                end = tramo.final

                while start < end:
                    next_t = min(start + 1, end)

                    sub_tramo = Tramo(start, tramo.tipo)
                    sub_tramo.final = next_t
                    sub_tramo.hilo = h

                    diagrama.elementos.append(sub_tramo)

                    start = next_t

            else:
                start = tramo.t

                while start < max_t:
                    next_t = min(start + 1, max_t)

                    sub_tramo = Tramo(start, tramo.tipo)
                    sub_tramo.final = next_t
                    sub_tramo.hilo = h

                    diagrama.elementos.append(sub_tramo)

                    start = next_t

                sin_fin = Tramo(max_t, tramo.tipo)
                sin_fin.hilo = h
                sin_fin.final = None
                diagrama.elementos.append(sin_fin)

    for s in diagrama.semaforos:
        s.x += diagrama.n_hilos
        for tramo in s.tramos:
            tramo.hilo = s

            if tramo.final is not None:
                    
                start = tramo.t
                end = tramo.final

                while start < end:
                    next_t = min(start + 1, end)

                    sub_tramo = Tramo(start, tramo.tipo)
                    sub_tramo.final = next_t
                    sub_tramo.hilo = s

                    diagrama.elementos.append(sub_tramo)

                    start = next_t

            else:
                start = tramo.t

                while start < max_t:
                    next_t = min(start + 1, max_t)

                    sub_tramo = Tramo(start, tramo.tipo)
                    sub_tramo.final = next_t
                    sub_tramo.hilo = s

                    diagrama.elementos.append(sub_tramo)

                    start = next_t

                sin_fin = Tramo(max_t, tramo.tipo)
                sin_fin.hilo = s
                sin_fin.final = None
                diagrama.elementos.append(sin_fin)

    diagrama.elementos.sort(key=lambda x: x.t)
    
def prueba(diagrama):
    agregar_tramos()
    labels_y_semaforos(diagrama)
    for e in diagrama.elementos:
        if isinstance(e,Tramo):
            print(f"TRAMO: hilo: {e.hilo.nombre}, inicio: {e.t}, fin: {e.final}, tipo: {e.tipo}")
        else:
            print(f"Tipo: {type(e).__name__}, hilo: {e.hilo.nombre}, t: {e.t}")

def a_manim(diagrama):
    agregar_tramos(diagrama)
    labels_y_semaforos(diagrama)
    t = 0
    while acciones_por_procesar(t, diagrama.elementos):
        #print(f"t = {t}")
        grupo = VGroup()
        for e in (elems for elems in diagrama.elementos if elems.t == t):
            match e:
                case Unaria():
                    #print(f"Accion")
                    grupo.add(a_manim_unaria(e))
                case Start():
                    #print(f"Start")
                    grupo.add(a_manim_start(e))
                case Sleep():
                    grupo.add(a_manim_sleep(e))
                case Join():
                    grupo.add(a_manim_join(e))
                case Await():
                    grupo.add(a_manim_await(diagrama, e))
                case Signal():
                    grupo.add(a_manim_signal(diagrama, e))
                case Tramo():
                    grupo.add(a_manim_tramo(e))
                case End():
                    grupo.add(a_manim_end(e))
        diagrama.grupos.append(grupo)
        t += 1
    return diagrama.grupos

def labels_y_semaforos(diagrama):
    grupo = VGroup()
    for h in diagrama.new_hilos:
        l = Text(f"{h.nombre}")
        visuales_nombres(l)
        l.move_to([h.x *3, 1, 2])
        grupo.add(l)
    for s in diagrama.semaforos:
        l = Text(f"{s.nombre}")
        visuales_nombres(l)
        l.move_to([s.x * 3, 1, 2])
        grupo.add(l)
    
    diagrama.grupos.append(grupo)

def a_manim_unaria(accion):
    label = Text(f"{accion.texto}")
    visuales_accion(label)
    label.move_to([(accion.hilo.x * 3), -accion.t*0.5, 2])
    caja = SurroundingRectangle(label)
    visuales_caja_accion(caja)
    return VGroup(label, caja)

def a_manim_start(start):
    label = Text(f"{start.hilo.nombre}.start({start.destino.nombre})")
    visuales_accion(label)
    label.move_to([(start.hilo.x * 3), -start.t*0.5, 2])
    caja = SurroundingRectangle(label)
    visuales_caja_accion(caja)
    flecha = crear_flecha(caja.get_right(), [start.destino.x * 3, -start.t*0.5, 0])
    label_creado = Text(f"{start.destino.nombre}")
    visuales_nombres(label_creado)
    label_creado.move_to([start.destino.x * 3, -start.t*0.5 + 0.5, 2])
    #visuales_flecha(flecha)
    return VGroup(label, caja, flecha, label_creado)

def a_manim_sleep(sleep):
    label = Text(f"{sleep.hilo.nombre}.sleep({sleep.duracion})")
    visuales_accion(label)
    label.move_to([(sleep.hilo.x * 3), -sleep.t*0.5, 2])
    caja = SurroundingRectangle(label)
    visuales_caja_accion(caja)
    return VGroup(label, caja)

def a_manim_join(join):
    label = Text(f"{join.hilo.nombre}.join({join.destino.nombre})")
    visuales_accion(label)
    label.move_to([(join.hilo.x * 3), -join.t*0.5, 2])
    caja = SurroundingRectangle(label)
    visuales_caja_accion(caja)
    return VGroup(label, caja)

def a_manim_await(diagrama, wait):
    label = Text(f"{wait.hilo.nombre}.await({wait.semaforo.nombre})")
    visuales_accion(label)
    label.move_to([(wait.hilo.x * 3), -wait.t*0.5, 2])
    caja = SurroundingRectangle(label)
    visuales_caja_accion(caja)
    c = visuals["green"] if wait.recurso_final > 0 else visuals["red"]
    new_rec = Text(f"{wait.recurso_final}")
    visuales_nombres(new_rec)
    new_rec.move_to([wait.semaforo.x * 3, -wait.t*0.5, 2])
    circle = Circle(color=c).move_to(new_rec.get_center_of_mass())
    visuales_circulo(circle)
    flecha = crear_flecha(caja.get_right(), circle.get_left(), visuals["red"])
    cola_text = cola_semaforo(wait)
    visuales_nombres(cola_text)
    cola_text.next_to(circle, RIGHT)
    return VGroup(label, caja, flecha, new_rec, circle, cola_text)

def a_manim_signal(diagrama, signal):
    label = Text(f"{signal.hilo.nombre}.signal({signal.semaforo.nombre})")
    visuales_accion(label)
    label.move_to([(signal.hilo.x * 3), -signal.t*0.5, 2])
    caja = SurroundingRectangle(label)
    visuales_caja_accion(caja)
    c = visuals["green"] if signal.recurso_final > 0 else visuals["red"]
    new_rec = Text(f"{signal.recurso_final}")
    visuales_nombres(new_rec)
    new_rec.move_to([signal.semaforo.x * 3, -signal.t*0.5, 2])
    circle = Circle(color=c).move_to(new_rec.get_center_of_mass())
    visuales_circulo(circle)
    flecha = crear_flecha(caja.get_right(), circle.get_left(), visuals["green"])
    cola_text = cola_semaforo(signal)
    visuales_nombres(cola_text)
    cola_text.next_to(circle, RIGHT)
    flecha_desbloqueo = None
    punto = None
    if signal.desbloquea_a:
        flecha_desbloqueo = crear_flecha([cola_text.get_x(), cola_text.get_y()-0.25, 0], [signal.desbloquea_a.x * 3, -signal.t*0.5-0.25, 0], visuals["green"])
        punto = Dot(color=visuals["green"]).move_to(flecha_desbloqueo.get_start()).scale(0.5)
    elementos = [label, caja, flecha, new_rec, circle, cola_text, flecha_desbloqueo, punto]
    return VGroup(*[elem for elem in elementos if elem is not None])

def a_manim_tramo(tramo):
    if isinstance(tramo.hilo, Semaforo):
        c = visuals["green"] if tramo.tipo == 'bien' else visuals["red"]
    else:
        if tramo.tipo == 'bien':
            c = visuals["color_tramo_bien"]
        if tramo.tipo == 'bloq':
            c = visuals["color_tramo_bloq"]
        if tramo.tipo == 'sleep':
            c = visuals["color_tramo_sleep"]

    if tramo.final:
        line = Line(start=[tramo.hilo.x * 3, -tramo.t*0.5, 0], end=[tramo.hilo.x * 3, -tramo.final*0.5, 0], color=c)
    else:
        line = Line(start=[tramo.hilo.x * 3, -tramo.t*0.5, 0], end=[tramo.hilo.x * 3, -tramo.t-50, 0], color=c)
    return line

def a_manim_end(end):
    g = VGroup()
    for j in end.hilo.joinedby:
        flecha = crear_flecha([end.hilo.x*3, -end.t*0.5, 0],[j.x*3, -end.t*0.5, 0])
        g.add(flecha)
    return g
    
def cola_semaforo(accion):
    if isinstance(accion, Await):
        text = ""
        for h in accion.cola_final:
            text += f"{h.nombre} "
        return Text(f"{text}", color=visuals["red"], disable_ligatures=True)
    else:
    # Construir texto con colores dinámicos
        s = accion.desbloquea_a
        t2c = {}  

        text = ""

        if s:
            text += f"{s.nombre} "
            t2c[s.nombre] = visuals["green"]

        for h in accion.cola_final:
            text += f"{h.nombre} "
            t2c[h.nombre] = visuals["red"]

    return Text(f"{text}", t2c=t2c, disable_ligatures=True)