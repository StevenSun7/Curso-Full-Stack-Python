# ESTRUCTURAS REPETITIVAS
# While
# EJERCICIO: Leer números y mostrarlos hasta que se ingrese un número negativo (ciclo condicional).
'''
num1 = int(input("Ingrese un número: "))
while num1 > 0:
    print(num1)
    num1 = int(input("Ingrese un número: "))
print("Fin del ejercicio")


# EJERCICIO: Desarrollar un programa que cuente hasta 4, utilizando una sola variable para contar (ciclo exacto).

cont = 1 #Inicializamos la variable
while cont <= 4:
    print(cont)
    cont = cont + 1     # Incrementamos la variable en 1
                        # Siempre debemos modificar la variable
                        # que determinará nuestra Condición
                        # Sino, se genera un CICLO INFINITO!
print("Fin del ejercicio")


# EJERCICIO: Ingresar números enteros y sumar solamente los números positivos, el programa finalizará ingresando 0 (cero) (ciclo condicional).

suma = 0
nro = int(input("Ingrese un número (cero para finalizar): "))
while nro != 0:
    if nro > 0:
        suma += nro #suma = suma + nro
    nro= int(input("Ingrese otro número (cero para finalizar): "))
print("FIN! Ingresó cero. La suma de los valores ingresados es:", suma)


# EJERCICIO: Ingresar 5 valores por teclado, obtener su suma y su promedio.
cont = 1
suma = 0
while cont <= 5:
    num= int(input("Ingrese un número: "))
    suma = suma + num   # Acumulamos, es equivalente suma += num 
    cont = cont + 1     # Incrementamos, es equivalente cont += 1

print("La suma es:", suma)
print("El promedio es:", suma/cont)


# Para el último ejemplo ¿qué debería hacer para que la cantidad de valores a ingresar la determine el usuario?, es decir: Ingresar una cantidad de valores definida por el usuario por teclado, obtener su suma y su promedio.

cont = 1
suma = 0
n= int(input("Ingrese la cantidad de valores a ingresar: "))
while cont <= n:
    num= int(input("Ingrese un número: "))
    suma = suma + num   # Acumulamos, es equivalente suma += num 
    cont = cont + 1     # Incrementamos, es equivalente cont += 1

print("La suma es:", suma)
print("El promedio es:", suma/cont)
'''
# Para el último ejemplo, preguntar: ¿qué debería modificar para preguntarle al usuario si desea ingresar más valores o no (ciclo condicional)?.

cont= 0
suma= 0
continuar = "S"
while continuar.upper() == "S":
    num= int(input("Ingrese un valor: "))
    suma = suma + num   # Acumulamos, es equivalente suma += num 
    cont = cont + 1     # Incrementamos, es equivalente cont += 1
    continuar = input("¿Desea continuar? S/N: ")

print("La suma es:", suma)
print("El promedio es:", suma/cont)
