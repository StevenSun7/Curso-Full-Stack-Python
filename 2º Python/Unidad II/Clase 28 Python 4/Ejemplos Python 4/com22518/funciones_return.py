# FUNCIONES QUE DEVUELVEN VALORES (return)

def restar(num1, num2):
    resta = num1-num2
    return resta

def cuadrado_de_par(num):
    if num % 2 ==0:
        print(num ** 2)
    else:
        return

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def es_par2(numero):
    return numero % 2 == 0

def cuadrado_y_cubo(numero):
    return numero ** 2, numero ** 3 

def operaciones(a,b):
    if b != 0:
        return a+b, a-b, a*b, a/b
    else:
        return a+b, a-b, a*b, "Error, b es 0"

#programa principal
suma, resta, multi, divi = operaciones(10,0)
print(suma)
print(resta)
print(multi)
print(divi)

 

'''
resultado = restar(10,3)
print("El resultado es:", resultado)
print("El resultado es:", restar(4,9))
cuadrado_de_par(8)
print(cuadrado_de_par(3))

print(es_par2(8))
print(es_par2(3))

for i in range(1,11):
    if es_par2(i):
        print(i,end=' ')


'''