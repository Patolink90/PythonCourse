serie = "N-02"

'''match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe")'''

cliente = {'nombre': 'Luis Ignacio',
           'edad': 34,
           'ocupacion': 'Ingeniero en sotware'}

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista': 'Keanu reeves',
                              'director': 'Lana & Lilly Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print(f"Es un cliente con la siguiente informacion.\n Nombre del cliente: {nombre} \n Edad: {edad} \n Ocupacion: {ocupacion} \n")
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print(f"Este elemento es una pelicula con la siguiente inormacion. \n")
            print(f"Protagonista: {protagonista} \n"
                  f"Director: {director}\n")
        case _:
            print("No se que es eso")