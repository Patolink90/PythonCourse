diccionario = {'c1':'valor1', 'c2':'valor1'}
#El siguiente guarda una coleccion de claves que tienen relacion con un usuario
diccionarioAndrea = {'c1':'Test', 'c100': 'Valor100'}

print(f'Este es el valor de la clave {diccionarioAndrea}')
#print(diccionario)
resultado = diccionario['c1']
#print(resultado)
cliente = {'nombre': 'juan', 'apellido': 'fuentes', 'peso': 88, 'altura' : 1.72}
consulta = cliente['apellido']
#print(consulta)

dic = {'c1': 55, 'c2':[10,20,30], 'c3':{'s1': 100, 's2': 200}}
#print(dic['c2'][1])
#print(dic['c3'])
#print(dic['c3']['s2'])

dic2 = {'c1':['a','b', 'c'], 'c2': ['d','e','f']}
#print(dic2['c2'][1].upper())

dic3 = {1:'a',2:'b'}
#print(dic3)
dic3[3] = 'c'
#print(dic3)
# sobreescribir claves en diccionario
dic3[2] = 'B'
#print(dic3)
#print(dic3.keys())
#print(dic3.values())
#print(dic3.items())

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
#print(mi_dict['puntos']['points2'][1])
