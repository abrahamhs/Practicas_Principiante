""" Write a function to return True if the first and last number
 of a given list is same. If numbers are different then return False. """

lista = [10, 20, 30, 40, 10]
indice = len(lista)
print(indice)
inicial = lista[0]
final = lista[len(lista)-1]
if inicial == final:
  print("True")
else:
  print("False")


  