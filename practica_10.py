# Dadas dos Listas con numeros crear una lista que contengan los valores impares de la primera
#  lista y los valores pares de la segunada lista.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
# resultados esperados result list: [25, 35, 40, 60, 90]

final_list = []
for i in range(len(list1)):
  if list1[i]%2 != 0:
    final_list.append(list1[i])
for i in range (len(list2)):
  if list2[i] % 2 == 0:
    final_list.append(list2[i])
print(f'El resultado de la lista es :{final_list}')
    

  
