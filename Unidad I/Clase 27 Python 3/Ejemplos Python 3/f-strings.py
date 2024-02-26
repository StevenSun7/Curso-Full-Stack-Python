#f-strings: ejemplo 1: cadenas
curso = 'Full Stack Python'
profesor = "Juan Pablo"
print(f'Estamos estudiando {curso} con {profesor}')
print()

#f-strings: ejemplo 2: números
base = 4
altura = 5
area = (4*5)/2
print(f'Base: {base}\nAltura: {altura}\nÁrea del triángulo: {area}')
print()

#f-strings: ejemplo 3
legajo = 12345
nombre = "Pablo"
apellido = "Picasso"
notas = [8, 7, 3]
promedio =sum(notas)/len(notas)

print(f"Legajo: {legajo}\nNombre completo: {apellido}, {nombre}\nNotas: {notas[0]}, {notas[1]}, {notas[2]}\nPromedio: {promedio}")
