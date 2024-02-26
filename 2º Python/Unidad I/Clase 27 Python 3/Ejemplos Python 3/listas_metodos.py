print("****** LISTAS: Métodos ******")

#Append / Insert
autores = ["Cortázar", "Borges", "Sábato"]
autores.append("Bioy Casares") #Agrega al final
print(autores)

musicos = ["León Gieco", "Fito Páez", "Carlos Gardel"]
musicos.insert(0, "Charly García") #Agrega al principio
print(musicos)

#Agregamos al final sin append
musicos.insert(len(musicos), "Astor Piazzola") #Mismo efecto (anidamos métodos)
print(musicos)

#Pop, Remove e Index
productos = ["Café", "Mate", "Azúcar", "Leche", "Mermelada", "Queso", "Galletitas"]
print(productos)
eliminado = productos.pop() #Elimina el último elemento
print("Se eliminó a:", eliminado)
print(productos)
eliminado = productos.pop(1) #Elimina el elemento en cierta pósición
print("Se eliminó a:", eliminado)
print(productos)

productos.remove("Azúcar")
print(productos)

print(productos.index("Leche")) #pos 1
#print(productos.index("Mate")) #Error: no lo encuentra porque fue eliminado

#Count, Reverse, Sort y Clear
numeros = [3,4,5,3,5,8,5]
print("Cantidad de 3:", numeros.count(3)) # El 3 está 2 veces
print("Cantidad de 7:", numeros.count(7)) #no está en la lista
print()

numeros = [2,4,6,7,5,9,8,12,15,1]
print("Original:", numeros)
numeros.reverse()
print("Reverse:", numeros) #Invierte la lista

numeros.sort()
print("Orden Ascendente:", numeros) #Orden de menor a mayor
numeros.sort(reverse=True)
print("Orden Descendente:", numeros) #Orden de mayor a menor

numeros.clear() #Vacía la lista
print(numeros)
print()

nombres = ['Juan','Ana','Luisa','Fernando']
print("Original:", nombres)
nombres.reverse()
print("Reverse:", nombres) #Invierte la lista

nombres.sort()
print("Orden Ascendente:", nombres) #Orden de A a Z
nombres.sort(reverse=True)
print("Orden Descendente:", nombres) #Orden de Z a A