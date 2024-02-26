print("****** CONJUNTOS ******")

#Creación de conjuntos
conj_uno = set()
conj_dos = {'Juan'}
conj_tres = {'Pablo', 3456, True}
conj_cuatro = {'Rivadavia', 3567, ('Calle 1', 'Calle2')}

print(conj_uno)
print(conj_dos)
print(conj_tres)
print(conj_cuatro)

#Acceso a elementos
conj_cinco = {2,5,6,9}
for i in conj_cinco:
    print(i, end=' ')
print()