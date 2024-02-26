#Ingresar datos con input
variable= input() #retorna un string
print("Hola", variable)

numero=int(input())
print(numero+1)

#Input con un parámetro de entrada
entrada= input("Ingrese su nombre: ") #podemos agregar un mensaje
print("Hola", entrada)
mje= "Ingrese un valor: "
entrada= input(mje) #podemos agregar una variable como mensaje
print("Hola", entrada)

#Otro ejemplo
lado=input("Ingresar el lado del cuadrado:")
superficie=lado*lado
print(superficie)

lado=int(input("Ingresar el lado del cuadrado:"))
#print("La superficie es "+ superficie) #Error
print("La superficie es "+ str(superficie))
print("La superficie es", superficie) #Otra forma