#Getters y Setters
class Color:

    def __init__(self):
        self.__color = 'Azul'

    @property #Getter
    def favorito(self):
        return f'Mi color favorito es: {self.__color}'

    @favorito.setter
    def favorito(self, bebida):
        self.__color = bebida

color1 = Color()
print(color1.favorito)
color1.favorito = 'Rojo'
print(color1.favorito)