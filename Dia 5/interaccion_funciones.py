from random import shuffle
#Lista inicial

palitos = ['-', '--', '---', '----']

#Mezclar palitos

def mezclar(lista):
    shuffle(lista)
    return  lista


#Perdirle intento

def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

#Comprobar intento

def check_intento(lista,intento):
    if lista[intento - 1] == '-':
        print('Pierdes y lavas los platos')
    else:
        print('Te salvaste maestro')

    print(f"Te ha tocado {lista[intento -1]}")

palitos_mezclados = mezclar(palitos)

seleccion = probar_suerte()

check_intento(palitos_mezclados,seleccion)