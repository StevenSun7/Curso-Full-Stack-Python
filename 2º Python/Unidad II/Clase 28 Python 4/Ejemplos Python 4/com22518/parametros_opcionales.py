def sumar(c=4,a=9,b=8):
    return a + b + c


def saludar(nombre, mensaje="encantado!"):
    print(f'Hola {nombre}, {mensaje}')

#programa principal
saludar(mensaje="¿Cómo estás?", nombre="Pedro")
saludar(nombre="María", mensaje="bienvenida a Codo a Codo!")
saludar("Juan", mensaje="¿cómo está el clima?")

'''
print(sumar(2,6))
print(sumar(2))
print(sumar(10))
print(sumar())
#print(sumar()) #Error
saludar("Juan Pablo")
saludar("Juan Pablo","¿cómo estás?")
'''


