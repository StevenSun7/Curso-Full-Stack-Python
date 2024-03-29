# Ámbito y ciclo de vida de las variables
def saludo(nombre):
    x = 10
    print(f'Hola {nombre}')
saludo('Luis')
print()
#print(x) # NameError: name 'x' is not defined

# -----------------------------------------
def muestra_x():
    x = 10
    print(f'x vale {x}')

x = 20 #Es una variable de alcance global, diferente de la que está dentro de la función
muestra_x() # x vale 10
print(x) #20
print()

# -----------------------------------------
y = 20 #Global 

def muestra_xy():
    x = 10 #Local
    y = 15 #Global modificada
    print(f'x vale {x}')
    print(f'y vale {y}')
muestra_xy() # "x" vale 10; "y" vale 15
print(y) #20, global