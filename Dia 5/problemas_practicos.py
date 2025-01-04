def devolver_distintos(num_a, num_b, num_c):
    lista = [num_a, num_c, num_b]
    if num_a + num_b + num_c > 15:
        return max(lista)
    elif num_a + num_b + num_c < 10:
        return min(lista)
    elif num_a + num_b + num_c in range(10, 15):
        lista.sort()
        minimo = min(lista)
        maximo = max(lista)
        lista.remove(minimo)
        lista.remove(maximo)
        return lista


def letras_unicas(palabra):
    lista = []
    for letra in palabra:
        if letra not in lista:
            lista.append(letra)
    lista.sort()
    return lista


def valida_cero_consecutivo(*args):
    contar = 1
    for n in args:
        if n > 0:
            contar = 0
        else:
            contar += 1

        if contar > 1:
            return True

    return False


def ceros_vecinos(*args):
    contador = 0

    for n in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False


def contar_primos(numero):
    contar = 0
    for n in range(3, numero, 2):
        if numero % n == 0:
            pass
        else:
            contar += 1
    return contar


def contar_primos_solved(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3, iteracion, 2):

            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)


print(contar_primos_solved(150))
