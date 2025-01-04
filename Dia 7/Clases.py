class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('Pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro ha volado una cantidad de {metros} metros')


    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")


#piolin = Pajaro('amarillo','canario')

Pajaro.poner_huevos(3)
Pajaro.mirar()