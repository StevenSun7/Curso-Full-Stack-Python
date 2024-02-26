# FUNCIONES CON PARÁMETROS
# Parámetros: Al definir la función
# Argumentos: Al invocarla / llamarla

# Funciones con un parámetro
def imprimir_mensaje_n_veces(n):
    for i in range(n):
        print("Mensaje", i)

# Funciones con dos parámetros
def imprimir_mensaje_personalizado(n, mje):
    for i in range(n):
        print(mje)

def multiplicar_por_5(numero):
    print(f'{numero}*5 = {numero * 5}')

#programa principal
#imprimir_mensaje_n_veces(10)
# imprimir_mensaje_personalizado(5, "Codo a Codo")
'''
veces = int(input("¿Cuántas veces vas a imprimir?: "))
while veces <= 0:
    print("Dato no válido!")
    veces = int(input("¿Cuántas veces vas a imprimir?: "))

#imprimir_mensaje_n_veces(veces)
mensaje = input("¿Cuál es el mensaje?: ")
while len(mensaje) == 0:
    print("Debe escribir un mensaje")
    mensaje = input("¿Cuál es el mensaje?: ")

imprimir_mensaje_personalizado(veces, mensaje)

'''

multiplicar_por_5(7)
multiplicar_por_5(125)
multiplicar_por_5(-9)