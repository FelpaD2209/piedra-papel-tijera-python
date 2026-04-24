nombre1 = input("¡Hola! Vos debes ser el jugador 1, ¿O como preferís que te llamen?: ")
nombre2 = input("Y vos serías el Jugador 2. ¿Como te llamas?: ")

cant_turnos = 0
cant_max_turnos = 3
Ganador = False

while not Ganador and cant_turnos < cant_max_turnos:

    Jugador1 = input(nombre1 + " ,¿Que elegís? ¿Piedra, papel o tijera?: ")
    Jugador2 = input("¿Y vos. " + nombre2 + "? ¿Que vas a hacer?: ")

    condicion1 = Jugador1 == "piedra" and Jugador2 == "tijera"
    condicion2 = Jugador1 == "tijera" and Jugador2 == "papel"
    condicion3 = Jugador1 == "papel" and Jugador2 == "piedra"
    
    if Jugador1 == Jugador2:
        print("Uh, empataron")
      
    elif condicion1 or condicion2 or condicion3:
        print("Ganó", nombre1)
    else:
        print("Ganó", nombre2)

    cant_turnos += 1

if cant_turnos >= cant_max_turnos:
    print("Listo, ya fue suficiente. Arreglense entre ustedes.")
    Ganador = True




      