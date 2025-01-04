from random import randint

player_name = input("Cual es tu nombre: ")

print(f"Bueno {player_name}, he pensado un número entre 1 y 100, y solo tienes ocho intentos "
      f"para adivinar cuál crees que es el número.")
contador = 0
numero = 0
aleatorio = randint(1,100)

while contador < 8:
    numero = int(input("Ingresa un número: "))
    contador += 1
    if numero < 1:
        print("Número no permitido, ingresa nuevamente: \n")
        numero = int(input("Ingresa un número: "))
    elif numero > 100:
        print("Numero excede el valor maximo permitido, ingrese nuevamente: \n")
        numero = int(input("Ingresa un número: "))
    elif numero < aleatorio:
        print("Mi numero es mas alto")
    elif numero > aleatorio:
        print("Mi numero es mas bajo")
    else:
        print(f"Haz adivinado el numero {aleatorio} en un total de {contador} intentos")
        break

if numero != aleatorio:
    print(f"Lo siento se han acabado los intentos, el número secreto era {aleatorio}")