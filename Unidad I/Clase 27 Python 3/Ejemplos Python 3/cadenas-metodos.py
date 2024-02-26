print("****** CADENAS: METODOS ******")

#Join 
cad="Juan Pablo"
cad='_'.join(cad)
print(cad) #Cadena devuelta con el separador _ entre cada caracter

#Split
cad="Cadenas de caracteres"
cad_lista=cad.split(' ') #Utiliza el espacio como separador
print(cad_lista) #Convierte la cadena en una lista
print(cad_lista[2]) #Podemos acceder a un elemento de esa lista

#Replace
cad="Programando en JavaScript. JavaScript es lo mejor!"
print(cad.replace('JavaScript', 'Python')) # reemplaza todas las apariciones

cad2="Programando en JavaScript. JavaScript es lo mejor!"
print(cad2.replace('JavaScript', 'Python', 1)) # reemplaza solo una aparición

#Count e Index
cad="Cadenas de caracteres"
print("Cantidad de c:", cad.count("c")) #2, no 3 porque es sensible a mayúsculas
print("Primer 'de':", cad.index("de")) #2
print("Primer 'de' (desde pos 3):", cad.index("de",3)) #8, desde pos 3

#isalpha / isdigit / isalnum
cad="Python"
cad2="Python3"
print(cad.isalpha()) # True
print(cad2.isalpha()) # False
print()
cad="1234"
cad2="1234a"
print(cad.isdigit()) # True
print(cad2.isdigit()) # False
print()
cad=""
cad2="1234"
cad3="ab"
cad4="12a"
print(cad.isalnum()) # False
print(cad2.isalnum()) # True
print(cad3.isalnum()) # True
print(cad4.isalnum()) # True
print()

#isupper / islower
cad="Python"
cad2="python"
print(cad.isupper()) # False
print(cad2.islower()) # True
print()

#center / ljust / rjust / zfill
cad1="Python"
cad2=cad1.center(14,"*")
print("Center:", cad2)# ****Python****
cad2=cad1.ljust(10, '-')
print("Ljust:", cad2)# Python---- 
cad2=cad1.rjust(10, '-')
print("Rjust:", cad2)# ----Python 
num=345
cad= str(num).zfill(7)
print("Zfill:", cad) # 0000345
print()

#lstrip / rstrip / strip
cad="---Hola-Python----"
print(cad)
print(cad.lstrip("-"))
print()

cad2="---Hola-Python----"
print(cad2)
print(cad2.rstrip("-"))
print()

cad3="*****Hola-Python****"
print(cad3)
print(cad3.strip("*"))
print()

#find y rfind
cad="Codo a Codo"
print(cad)
print(cad.find("Codo")) #Desde la izquierda
print(cad.rfind("Codo")) #Desde la derecha