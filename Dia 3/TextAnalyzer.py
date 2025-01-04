texto = input("Ingresa el texto que quieras: ")
letras_busqueda = []
letras_busqueda.append(input("ingresa la primer letra que desees buscar en el texto anterior: "))
letras_busqueda.append(input("ingresa la segunda letra que desees buscar en el texto anterior: "))
letras_busqueda.append(input("ingresa la tercer letrs que desees buscar en el texto anterior: "))
texto.lower()

print(f"Estas son las letras que ingresaste: {letras_busqueda}")

total_letras1 = texto.count(letras_busqueda[0])
total_letras2 = texto.count(letras_busqueda[1])
total_letras3 = texto.count(letras_busqueda[2])

print(f"Total de veces que aparecen la letra '{letras_busqueda[0]}' en el texto: {total_letras1} \n")
print(f"Total de veces que aparecen la letra '{letras_busqueda[1]}' en el texto: {total_letras2} \n")
print(f"Total de veces que aparecen la letra '{letras_busqueda[2]}' en el texto: {total_letras3}\n")

mi_lista = texto.split(" ")
print(f"Este es el numero de palabras en el texto {len(mi_lista)}")
print(f"Esta es la primer letra del texto: {texto[0]} y esta es la ultima letra del texto: {texto[-1]}")
mi_lista.reverse()
texto_inverso = " ".join(mi_lista)
print(f"Este es el texto con las palabras a la inversa: {texto_inverso}")
buscar_python = 'Python' in texto
diccionario = {True:"si", False:"no"}
print(f"Aparece la palabra Python en el texo?: {diccionario[buscar_python]}")


