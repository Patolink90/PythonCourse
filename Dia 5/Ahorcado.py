from random import choice

lista_palabras = ['gato','perro','hormiga','elefante','vaso']
lista_letras_validas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
lista_letras_incorrectas = []
lista_adivinada = []
letra_ingresada = ''
vidas = 6


def elige_palabra_azar(lista):
    palabra = choice(lista)
    return palabra

def mostrar_guiones(palabra):
    guiones = ''
    for letra in palabra:
        guiones += '_ '
    return guiones

palabra = elige_palabra_azar(lista_palabras)
guiones = mostrar_guiones(palabra)
print(guiones)

def valida_letra(letra,palabra,vidas):
    if letra not in lista_letras_validas:
        pedir_letra()
    else:
        letra_correcta = ''
        if len(lista_adivinada) == 0:
            if letra in palabra:
                for l in palabra:
                    if l != letra:
                        letra_correcta += '_ '
                    else:
                        letra_correcta += l + ' '

                lista_adivinada.append(letra_correcta.split(' '))
            else:
                lista_letras_incorrectas.append(letra)
                vidas -= 1
                print(f"letra/s incorrectas: {lista_letras_incorrectas}\n")
                print(f"vidas restantes: {vidas}")
        else:
            if letra in palabra:
                for elem in lista_adivinada[letra.index()]:
                    if letra != elem:
                        lista_adivinada.insert(elem,letra)
            pass


    return lista_adivinada



#print(valida_letra('a',palabra,vidas))


def pedir_letra():
    letra_ingresada = ''
    while vidas > 0:
        letra_ingresada = input("Ingresa una letra: ")
        valida_letra(letra_ingresada,palabra,vidas)
    else:
        return "Fin del juego"


pedir_letra()