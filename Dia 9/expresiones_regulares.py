import re


#clave = input("Clave: ")

patron = r'\D{1}\w{7}'

email_patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

email = "my.ownsite@our-earth.org"

valid = re.match(email_patron, email)

print("Valid email address." if valid else "Invalid email address.")

#chequear = re.search(patron, clave)

#print(chequear)

texto = "No atendemos los lunes por la tarde"

buscar = re.search(r'lunes|martes', texto)
print(buscar)

buscar = re.search(r'.demos', texto)
print(buscar)

buscar = re.search(r'....demos...', texto)
print(buscar)

buscar = re.search(r'Hola', "Hola")
print(buscar)

buscar = re.search(r'^\D', texto)
print(buscar)

buscar = re.search(r'\D$', texto)

print(buscar)

buscar = re.findall(r'[^\s]+', texto)

print(''.join(buscar))