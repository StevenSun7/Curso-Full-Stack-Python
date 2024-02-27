class Persona: 
    edad=20

    def __init__(self, nombre):
        self.nombre=nombre

# Bloque principal
persona1=Persona("Juan") 
persona2=Persona("Ana") 
persona3=Persona("Luis") 

print(persona1.nombre) # Juan
print(persona2.nombre) # Ana
print(persona3.nombre) # Luis
print()
print("Edad de la persona1:", persona1.edad) # 20
print()
Persona.edad=5 #Afecta a toda la clase
print("Modificamos la variable edad (variable de CLASE) con el valor", Persona.edad)
print(persona1.edad) # 5
print(persona2.edad) # 5
print(persona3.edad) # 5
print()
print("Solo modificamos la variable edad para ESTE OBJETO")

persona3.edad=15 #Afecta al objeto
print("Edad de la persona3:",persona3.edad) # 15
