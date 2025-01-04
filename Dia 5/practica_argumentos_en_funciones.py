def suma_cuadrados(*args):
    total = 0
    for n in args:
        total += n * n
    return total


def suma_absolutos(*args):
    total = 0
    for n in args:
        if n < 0:
            total += (n * -1) * (n * -1)
        else:
            total += n * n
    return total


def numeros_persona(nombre, *args):
    suma_numeros = 0
    for n in args:
        suma_numeros += n
    return f"{nombre}, la suma de tus numeros es {suma_numeros}"


# se viene ejemplos usando **kwargs

def suma(**kwargs):
    # print(type(kwargs)) --->> <class 'dict'>
    total = 0
    for clave, valor in kwargs.items():
        total += valor
        print(f"{clave} = {valor}")
    return total


print(suma(x=3, y=5, z=3))


def suma_b(num1, num2, *args, **kwargs):
    print(f'el primer valor es {num1}')
    print(f'el segunfo valor es {num2}')

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


suma_b(2, 5, 12, 12, 33, 232, 2343, 5345, 65546, x='uno', y='dos', z='tres')

args = [12, 33, 232, 2343, 5345, 65546]
kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}

suma_b(12, 3244, *args, **kwargs)


def cantidad_atributos(**kwargs):
    contar = 0
    for kwarg in kwargs:
        contar += 1
    return contar


def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}\n")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


describir_persona('pato',color_ojos="azules", color_pelo="rubio")