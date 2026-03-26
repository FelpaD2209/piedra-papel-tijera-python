import random

numero_secreto = random.randint(1,101)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("""¿Que haces, locura? ¿Queres jugar a algo?
A ver, ¿que número estoy pensando? """)

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("Elegí un número entre el 1 y el 100: ")
    numero = int(entrada.strip())

    if numero == numero_secreto:
        print("Bue pará Akinator, ¿Como hiciste? Felicitaciones, le pegaste.")
        adivinado = True
    elif numero < numero_secreto:
        print("Un poco más arriba.")
    else:
        print("Menos, menos.")       

    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print("¡Listo, finite! Mejor suerte para la próxima.")         


