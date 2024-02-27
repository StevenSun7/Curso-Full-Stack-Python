# Propagación de excepciones
def funcion(x, y):
  print("antes")
  try:
    div = x/y # Excepción!
  except:
    div = "Algo salió mal"
  print("después")
  return div

def main():
  x = float(input('x: '))
  y = float(input('y: '))
  print(funcion(x, y))
  print("listo")

# Programa principal
main()