# Propagación de excepciones
'''
Durante la ejecución de un programa, si dentro de una función surge una excepción
y la función no la maneja, la excepción se propaga hacia la función que la invocó,
si esta otra tampoco la maneja, la excepción continua propagándose hasta llegar a
la función inicial del programa y si esta tampoco la maneja se interrumpe la
ejecución del programa
'''

def f(x, y):
     return x / y

def g(x, y):
    return f(x, y)

#Programa principal
z = g(5, 0)
print(z)