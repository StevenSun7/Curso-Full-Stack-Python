print("Tipos de conversión")
print()

# str -> int
print("str -> int:",int("123")) #Con 123a da error
# int -> str
print("int -> str: " + str(289)) #Si queremos sumar un valor numérico da error

# str -> float
print("str -> float:",float("123.12"))
# float -> str
print("float -> str:", str(123.12))

# int -> float
print("int -> float:", float(145)) #Agrega el 0
# float -> int
print("float -> int:", int(1373.12)) #Trunca el dato, conserva la parte entera, no es lo mismo que redondear.
