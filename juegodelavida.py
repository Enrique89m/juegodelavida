
import copy, random, sys, time

anchoBoolean = False
altoBoolean = False

while not anchoBoolean:
    print("Indica el ancho de la cuadrícula (de 10 a 100)")
    numero1 = int(input())
    if 10 <= numero1 <= 100:
        ancho = numero1
        anchoBoolean = True
    else:
        print("El ancho debe ser de 10 a 100")

while not altoBoolean:
    print("Indica el alto de la cuadrícula (de 5 a 30)")
    numero2 = int(input())
    if 5 <= numero2 <= 30:
        alto = numero2
        altoBoolean = True
    else:
        print("El alto debe ser de 5 a 30")

vivoBoolean = False

while not vivoBoolean:
    print("Ahora indica el caracter para identificar las células vivas")
    caracterVivo = input()
    if len(caracterVivo) != 1:
        print("Debes introducir un caracter válido")
    else:
        vivo = caracterVivo
        vivoBoolean = True


MUERTO = ' '   # Carácter para la celda muerta

# Las variables celulas y siguientesCelulas son diccionarios que contienen
# el estado actual del juego y el siguiente.
# Las claves del diccionario son tuplas que pueden tener el valor VIVO o MUERTO
siguientesCelulas = {}

# Asignamos valores aleatorios a las células iniciales
for x in range(ancho):
    for y in range(alto):
        # 50% de posibilidades de estar viva o muerta
        if random.randint(0, 1) == 0:
            siguientesCelulas[(x, y)] = vivo
        else:
            siguientesCelulas[(x, y)] = MUERTO

while True:  # bucle principal del programa
    # Cada iteración de este bucle es una generación de la simulación del juego de la vida

    print('\n' * 50)  # Separación entre generaciones
    celulas = copy.deepcopy(siguientesCelulas)

    # Imprimimos las células por pantalla
    for y in range(alto):
        for x in range(ancho):
            print(celulas[(x, y)], end='')
        print()
    print('Pulsa Ctrl-C para parar.')

    # Calculamos la nueva generación de células en función de los valores actuales
    for x in range(ancho):
        for y in range(alto):
            # Obtenemos las coordenadas de las vecinas incluso si están en el límite
            izquierda = (x - 1) % ancho
            derecha = (x + 1) % ancho
            arriba = (y - 1) % alto
            abajo = (y + 1) % alto

            # Calculamos el número de células vecinas vivas
            numVecinasVivas = 0
            if celulas[(izquierda, arriba)] == vivo:
                numVecinasVivas += 1
            if celulas[(x, arriba)] == vivo:
                numVecinasVivas += 1
            if celulas[(derecha, arriba)] == vivo:
                numVecinasVivas += 1
            if celulas[(izquierda, y)] == vivo:
                numVecinasVivas += 1
            if celulas[(derecha, y)] == vivo:
                numVecinasVivas += 1
            if celulas[(izquierda, abajo)] == vivo:
                numVecinasVivas += 1
            if celulas[(x, abajo)] == vivo:
                numVecinasVivas += 1
            if celulas[(derecha, abajo)] == vivo:
                numVecinasVivas += 1

            # Basamos el valor de la nueva generación en función
            # de los valores actuales
            if celulas[(x, y)] == vivo and (numVecinasVivas == 2
                                            or numVecinasVivas == 3):
                    # Cálulas vivas con 2 o 3 vecinas vivas permanecen vivas
                    siguientesCelulas[(x, y)] = vivo
            elif celulas[(x, y)] == MUERTO and numVecinasVivas >= 2:
                # Células muertas con 3 vecinas vivas cobran vida
                siguientesCelulas[(x, y)] = vivo
            else:
                # En cualquier otro caso continuan muertas
                siguientesCelulas[(x, y)] = MUERTO

    try:
        time.sleep(1)  # Añadimos un segundo de pausa para evitar parpadeos
    except KeyboardInterrupt:
        print("Juego de la vida de Conway")
        print("https://es.wikipedia.org/wiki/Juego_de_la_vida")
        sys.exit()  # Cuando se pulsa CTRL+C termina el programa
