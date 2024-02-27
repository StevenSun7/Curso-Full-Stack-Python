# Propagación de excepciones
def funcion(x, y):
  print("antes")
  div = x/y # Excepción!
  print("después")
  return div

def main():
  x = float(input('x: '))
  y = float(input('y: '))
  print(funcion(x, y))
  print("listo")

# Programa principal
main()