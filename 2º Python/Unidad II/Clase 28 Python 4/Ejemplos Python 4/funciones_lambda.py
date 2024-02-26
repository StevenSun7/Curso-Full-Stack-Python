
cuadrado = lambda x: x ** 2
# ---------------------------------
def alCubo(x): #definición de función común
    return x*x*x

#Programa principal
cubo = lambda x: x*x*x # la misma función escrita 
                       # como función lambda, no tiene nombre,
                       # es anónima (ojo: cubo es el nombre de la variable, no de la función)
print(alCubo(3)) #27
print(cubo(5)) #125 

# ---------------------------------
# Usamos una función anónima en combinación con map()
enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))
print(cuadrados) # [1, 4, 16, 49]

# ---------------------------------
# Ejemplo: en lugar de pasar una lista de valores, pasamos como segundo parámetro una lista de funciones
enteros = [1, 2, 4, 7,]
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3

funciones = [cuadrado, cubo] #lista de funciones
for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores) # [1, 1] [4, 8] [16, 64] [49, 343]