# Cadenas de caracteres
dia="Martes"
mes='Noviembre'
print(dia+mes)
print(dia,mes)

apellido="Martínez"
print(apellido[0])
print(len(apellido))
posUltimoCaracter = len(apellido)-1 #Es -1 porque arranca de 0.
print(apellido[posUltimoCaracter])

#Programa para obtener el primer caracter, el último y el largo de la cadena
nombre = input("Ingrese su nombre: ")
primer_caracter = nombre[0]
largo_cadena = len(nombre)
ultimo_caracter= nombre[largo_cadena-1]
# ultimo_caracter= nombre[-1]
print("--------- INFORME ---------")
print("Primer caracter:", primer_caracter)
print("Último caracter:", ultimo_caracter)
print("Largo de la cadena:", largo_cadena)

nombre_completo="carlos Martínez estrada"
print(nombre_completo.lower()) #minúsculas
print(nombre_completo.upper()) #mayúsculas
print(nombre_completo.capitalize()) #primer letra de la cadena
print(nombre_completo.title()) #primer letra de cada palabra