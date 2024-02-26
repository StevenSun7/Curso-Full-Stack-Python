print("****** LISTAS: Operaciones ******")

#Concatenar
paises= ["Argentina", "Uruguay", "Brasil"]
ciudades= ["Buenos Aires", "Montevideo", "San Pablo"]
todos=paises + ciudades
print(todos)
print(paises + ["Venezuela"]) #Concatena, no agrega
print(paises) #No fue agregado Venezuela
print()

#Modificar valores por posición
provincias = ["Mendoza", "Jujuy", "Salta"]
print(provincias) #Original
provincias[2]="Córdoba"
print(provincias) #Cambiada

#Intercambiar valores
aux = provincias[0]
provincias[0] = provincias[2]
provincias[2] = aux
print(provincias)
print()

#len (largo de la lista)
print("Cantidad de provincias:", len(provincias))

#Suma, máximo, mínimo y promedio
notas= [3,10,9,8,7,5]
print("Notas:", notas)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas)) 
print("Suma de notas:", sum(notas))
print("Promedio:", sum(notas)/len(notas))

#list / in - not in
cadena=list("Hola")
print(cadena)
numeros=list(range(4))
print(numeros)

print("o" in cadena)
print("H" not in cadena)

print(2 in numeros)
print(1 not in numeros)