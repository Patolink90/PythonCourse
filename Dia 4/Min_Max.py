#menor = min(20,19,90,100,2,7)

#mayor = max(20,19,90,100,2,7)

lista = [20,19,90,100,2,7]

print(f'El menor es  {min(lista)} y el mayor es {max(lista)}')

#print(menor)
#print(mayor)

nombres = ['juan','pablo','alicia', 'carlos']

nombre = 'Carlos' # 'carlOs'
nombreb = 'carlos'

print(min(nombreb))
print(min(nombre.lower())) # se usa lower para descartar el caso de la busqueda por mayusculas en primer termino
print(min(nombres))


diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = (min(diccionario_edades.values()))

ultimo_nombre = (min(diccionario_edades))