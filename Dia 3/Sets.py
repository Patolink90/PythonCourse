mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

# print(mi_set[0])
# este set no se puede acceder como lista o diccionario por que los elementos no son subscribiles

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

s3 = mi_set.union(otro_set)
s3.add(10)
s3.remove(1)
# s3.remove(11)
s3.discard(11)
# s3.pop()
# s3.clear()
print(s3)