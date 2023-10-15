print("""Ejercicio 1 : Given two integer numbers, return their product
only if the product is equal to or lower than 1000. Otherwise, return their sum.""")
number1 = int(input('\nIngrese el primer nuemro: \n'))
number2 = int(input('\nIngrese el segundo numero: \n'))
producto = number1 * number2

if producto <= 1000:
  print('El producto de los numeros es', producto)
else:
  producto = number1 + number2
  print ('\nEl resultado del producto es:', producto, '\n')
  
  
if producto < 1000:
  print('Producto menor que 1000')
  
elif (producto >= 100) & (producto <= 2000):
  print('Producto mayor que 1000 y menor que 2001')
else :
  print('Producto MAYOR que 2001')