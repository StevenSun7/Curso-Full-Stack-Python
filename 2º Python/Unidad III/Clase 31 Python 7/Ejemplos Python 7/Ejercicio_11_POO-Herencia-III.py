class Padre(): #Superclase 1

    def __init__(self):
        self.apellido = "Pérez"

    def llevar(self):
        print(f'Papá me lleva al colegio')

    # def programar(self):
    #     print(f'Papá programa en JAVA')

class Madre(): #Superclase 2
    def __init__(self):
        self.apellido = "Osorio"

    def programar(self):
        print(f'Mamá programa en Python')
    
class Hijo(Padre, Madre): #Subclase
    nombre = ""

    def amar(self):
        print(f'Soy {self.nombre} {self.apellido} y amo a mis padres')

hijo1 = Hijo() # Instancia de Hijo
hijo1.nombre = "Fernando"
hijo1.llevar() # Método del padre
hijo1.programar() # Método de la madre
hijo1.amar() # Método propio