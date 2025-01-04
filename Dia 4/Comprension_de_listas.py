palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)
#el codigo de arriba es de la manera tradicion
#el codigo siguiente es con el concepto de comprension de listas
#basicamente se usa para contruir una lista a partir de un ciclo for de manera mas optima
lista2 = [letra for letra in palabra]
lista3 = [letra for letra in 'python']
lista4 = [n for n in range(0,21,2)]
lista5 = [n / 2 for n in range(0,21,2)]
lista6 = [n for n in range(0,21,2) if n * 2 > 10]
#implementando con else se vuelve un poco mas complejo y hay que mover el orden del if al inicio para poder acompaniarlo de la instruccion else
lista7 = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
#print(lista3)
#print(lista4)
#print(lista5)
#print(lista6)
#print(lista7)

pies = [10,20,30,40,50]

metros = [n / 3.281 for n in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [n for n in valores if n % 2 == 0]

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(n - 32) * (5/9) for n in temperatura_fahrenheit]