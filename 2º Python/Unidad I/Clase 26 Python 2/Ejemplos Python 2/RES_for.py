# ESTRUCTURAS REPETITIVAS
# for
# EJERCICIO: Mostrar los números del 1 al 10.

for i in range(1,11,1): #No incluye al 10 (se puede poner 10+1)
    # print(i)
    print(i, end=' ')

# EJERCICIO: Mostrar los múltiplos de 5 comprendidos entre 15 y 80.

for i in range(15,81,5):
    print(i)

# EJERCICIO: Imprimir los números del 9 al 1.

for i in range(9,0,-1): # En este caso, como el valor inicial 
                        # es mayor al valor final, el paso debe 
                        # ser necesariamente un número negativo.
    print(i)

# EJERCICIO: Mostrar los números del 10 al 20.

for i in range(10,21):
    print(i)

# EJERCICIO: Ingresar cinco números y mostrar su suma.

suma = 0
for i in range(5):
    a = int(input("Ingrese un número: "))
    suma += a #suma = suma + a
print("La suma es:", suma)