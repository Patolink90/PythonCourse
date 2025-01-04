from random import randint, choice


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return (dado1, dado2)


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


def reducir_lista(lista):
    lista_numeros = []
    elemento_mayor = 0
    for n in lista:
        if n not in lista_numeros:
            lista_numeros.append(n)

    for n in lista_numeros:
        if elemento_mayor == 0:
            elemento_mayor = n
        elif n > elemento_mayor:
            elemento_mayor = n

    lista_numeros.remove(elemento_mayor)

    return lista_numeros


# print(reducir_lista([1,2,15,7,2]))

def promedio(lista):
    resultado = 0
    for n in lista:
        resultado += n

    resultado = resultado / len(lista)
    return resultado


def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    resultado = choice(moneda)
    return resultado


def probar_suerte(moneda,lista):
    if moneda == 'Cara':
        lista.clear()
        print(f"La lista se autodestruirá:{lista}")
        return lista
    else:
        print(f"La lista fue salvada {lista}")
        return lista

moneda = lanzar_moneda()
print(probar_suerte(moneda,[1,2,3,4,5]))