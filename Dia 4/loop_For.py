listta = ['a','b','c']

for letra in listta:
    numero_letra = listta.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")


nombres = ['pablo','laura','fede','luis','julia']
print('\nsegundo ejemplo \n')
for nombre in nombres:
    if nombre.startswith('l'):
        print(nombre)

print('\nTercer ejemplo \n')

numeros = [1,2,3,4,5]

mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

print('\nIterar strings ejemplo \n')

palabra = 'python'
numero_letra = 0
for letra in palabra:
    numero_letra = numero_letra + 1
    print(f"letra: {numero_letra}: {letra}")

print('\niterar objetos ejemplo \n')
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print('\niterar diccionarios ejemplo \n')

dic = {'clave1':'a', 'clave2':'b', 'clave3': 'c'}

for item in dic.values():
    print(item)

for item in dic.items():
    print(item)
print('\n')
for a,b in dic.items():
    print(a,b)
#Practica
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print('Hola ' + alumno)
#Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:"""
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
    #print(suma_numeros)

#Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:
#Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar
#num % 2 == 0 (valores pares)
#num % 2 == 1 (valores impares)#
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if (numero % 2 == 0):
        suma_pares = suma_pares + numero
    elif (numero % 2 == 1):
        suma_impares = suma_impares + numero