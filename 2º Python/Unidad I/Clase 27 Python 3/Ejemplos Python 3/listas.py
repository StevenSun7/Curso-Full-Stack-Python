print("****** LISTAS ******")

#Creación e impresión de listas
mundiales = [2010,2014,2018,2022] #Lista de números
apellidos = ["García", "López", "Rodríguez"] #Lista de strings
vacia= [] #Lista vacía
mixta = ['Juan', 37, True, 12.75]
lista_de_listas= [[1,3,5],[2,4,6]] #Listas anidadas

print(mundiales)
print(apellidos)
print(vacia)
print(lista_de_listas) 
print()

#Acceso a elementos
print(mundiales[0]) #Primero
print(mundiales[-1]) #Último
print(mundiales[3]) #Cuarto (recordemos empieza en 0)
#print(mundiales[4]) #Error out of range
print(lista_de_listas[0]) 
print(lista_de_listas[1][2])
print()


# Iterar sobre una lista (for)
vocales=['a','e','i','o','u']
for i in vocales:
    # print(i, end="-")
    print(i)
print()

# Iterar sobre una lista (while)
i = 0
while i < len(vocales):
    # print(vocales[i], end="-")
    print(vocales[i])
    i += 1 #i = i+1
print()

#Desempaquetado de listas
animales= ["Perro", "Gato", "Tortuga"] 
ani1, ani2, ani3 = animales #Dsempaquetamos: asignamos a cada variable un elemento de la lista
print(ani1)
print(ani2)
print(ani3)

lista_de_listas= [['Juan','Pablo','Luis'],['Ana','Laura','Noelia']] #Listas anidadas
lista1, lista2 = lista_de_listas #Desempaquetamos las listas
print(lista1)
print(lista2)
v1L1, v2L1, v3L1 = lista1 #Desempaquetamos la primer lista
print(v2L1)