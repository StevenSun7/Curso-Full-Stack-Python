# IMPORTAR UNA FUNCIÓN
from saludos import saludar
saludar()
print()
#saludar_dos("Juan Pablo") #Error, no fue importada

# IMPORTAR TODAS LAS FUNCIONES
from saludos import *
saludar_dos("Juan Pablo") 
print()
saludar_tres("Buenos Aires") #si no hubiese importado todas las funciones no la podría usar
print()
sld = Saludo("Nardone", "Juan Pablo")

# Otra forma de importar:
# import saludos





