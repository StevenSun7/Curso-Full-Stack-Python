print("****** CADENAS DE CARACTERES ******")
#Escritura y concatenación
cadena1 = "Aprendiendo cadenas de caracteres "
cadena2= 'en Codo a Codo'
print(cadena1) 
print(cadena2)
print(cadena1 + cadena2 + " con Juan Pablo")
#Concatenar números y cadenas
edad = 20
altura = 1.70
datos= "La edad es " + str(edad) + " y la altura es " + str(altura)
print(datos) 
print("La edad es", edad, "y la altura es", altura)

# Combinar comillas simples y dobles
print("Nuestro profesor se llama 'Juan Pablo'")
print('Nuestro profesor se llama "Juan Pablo"')

#Replicación de cadenas
risa='ja'
carcajada=risa*5
print(carcajada)
print("-"*10)


#Cadenas multilínea
cadena = """Cadenas
en más
de una 
línea """
cadena2 = '''Cadena multilínea
con comillas
simples'''
print(cadena)
print(cadena2)

#Comparación de cadenas (ASCII y case sensitive)
cad1 = "@" # 64
cad2 = "^" # 94
cad3 = "@" # 64
print(cad1 > cad2)
print(cad1 < cad2)
print(cad1 == cad3)

ciudad = "Córdoba"
if ciudad == "Córdoba":
    print("El envío llegará mañana")
else:
    print("El envío llegará pasado mañana")

#Largo de cadenas y subíndices
nombre = "Juan Pablo"
print(len(nombre))
print(nombre[0]) # Primer caracter
print(nombre[-1]) # Último caracter
print(nombre[len(nombre)-1]) # Último caracter

#Métodos upper / lower / capitalize / title
cad = "Estamos aprendiendo Python"
print(cad.upper()) # Mayúsculas
print(cad.lower()) # Minúsculas
print(cad.capitalize()) # Primera letra mayúscula
print(cad.title()) # Primera letra de cada palabra


#Rebanadas (slicing)

# [:] Todos los elementos.
cadena="Aprendiendo Python"
print(cadena[:])

# [start:] Todos los elementos desde el índice establecido(start).
print(cadena[12:]) #Desde el 12

# [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
print(cadena[:3]) #No incluye pos 3

# [start:end] Todos los elementos de un rango de índices.
print(cadena[1:11]) #No incluye pos 11

# [start:end:step] Todos los elementos de un rango de índices con saltos.
print(cadena[6:11:2])

# [::step] Todos los elementos con saltos.
print(cadena[::3])

# [::step] Todos los elementos con saltos (negativo).
print(cadena[::-1])

#Operadores de pertenencia: in / not in

cadena="Aprendiendo Python"
print("A" in cadena) # True
print("z" in cadena) # False
print("prendiendo" in cadena) # True
print("D" not in cadena) # True
print("o" not in cadena) # False


#Iterando cadenas
#For
cad = "Python"
for letra in cad:
    print(letra)
    #print(letra,end='')
print()

#While
i = 0
while i < len(cad):
    print(cad[i])
    #print(cad[i],end='')
    i += 1 #i = i + 1
#Uso de min y max
cadena = "Python"
print(min(cadena)) # 80
print(max(cadena)) # 121 
