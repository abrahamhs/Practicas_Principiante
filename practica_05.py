""" Write a function to return True if the first and last number
 of a given list is same. If numbers are different then return False. """
# creo una funcion que toma una lista como parametro y imprime la lista, 
# su tamaño, primer y ultimo elemento ademas de comparar si son iguales o diferentes
def list_compare(list):
  indice = len(list)
  print(f'Datos internos de la lista : {list}')
  print(f'Elementos en la lista : {indice} ' )
  print("First element: ", list[0])
  print("Last element: ", list[-1])
  inicial = list[0]
  final = list[len(list)-1]
  if inicial == final:
    print("True \n")
  else:
    print("False\n")

lista1 = [10, 20, 30, 40, 30, 10]
lista2 = [40, 20, 30, 40, 70, 80, 60]

list_compare(lista1)
list_compare(lista2)

  