# ESTRUCTURAS CONDICIONALES
# if 
# EJERCICIO: Ingresar un número y determinar si es menor que 10.

a=float(input("Ingrese un número: "))
if a < 10:
    print("El número ingresado es menor que 10")
print("Fin del programa") #Fuera del if
# if .. else
# EJERCICIO: Ingresar un número distinto de cero y decir si es par o impar.

b=int(input("Ingrese un número distinto de cero: "))
if b % 2 == 0:
    print(b, "es par") #Bloque de verdad: Si se cumple la condición
else:
    print(b, "es impar") #Si NO se cumple la condición

# Estructuras condicionales anidadas / if .. elif .. else
# EJERCICIO: Ingresar un número entero e imprimir un mensaje indicando si es cero, par o impar.

c=int(input("Ingrese un número: "))
if c == 0:
    print("El número ingresado es cero.")
else:
    if c % 2 == 0:
        print("El número", c, "es par.")
    else:
        print("El número", c, "es impar.") #No es par ni cero

# Leer un número entero e imprimir un mensaje de acuerdo al valor ingresado:
# a) Si ingresa 1 debe mostrar “Ingresando a depósitos…” 
# b) Si ingresa 2 debe mostrar “Ingresando a extracciones…”
# c) Si ingresa 3 debe mostrar “Pago de tarjeta”
# d) En el caso de ingresar otro número debe aparecer “Opción incorrecta”.

op=int(input("Ingrese una opción entre 1 y 3: "))
if op == 1:
    print("Ingresando a depósitos…")
else:
    if op == 2:
        print("Ingresando a extracciones...")
    else:
        if op == 3:
            print("Pago de tarjeta")
        else:
            print("Opción incorrecta")

op=int(input("Ingrese una opción entre 1 y 3: "))
if op == 1:
    print("Ingresando a depósitos…")
elif op == 2:
    print("Ingresando a extracciones...")
elif op == 3:
    print("Pago de tarjeta")
else:
    print("Opción incorrecta")

# Uso de operadores lógicos (AND y OR)
# AND
# EJERCICIO: Ingresar un número y decir si tiene de dos cifras o no.
 
e=int(input("Ingrese un número: "))
if e >=10 and e <= 99:
    print("El número ingresado es de dos cifras")
else:
    print("El número ingresado no tiene dos cifras")

#Se puede abreviar usando la siguiente notación:
if 10 <= e <= 99:
    print("El número ingresado es de dos cifras")
else:
    print("El número ingresado no tiene dos cifras")

# OR
# EJERCICIO: Ingresar un número entero y decir si es divisible por 6 o 2
num1=int(input("Ingrese un número: "))
if num1 % 6 == 0 or num1 % 2 == 0:
    print(num1, "es divisible por 6 o 2")
else:
    print(num1, "NO es divisible por 6 ni 2")