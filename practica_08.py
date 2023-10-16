# Print the following pattern
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

"""
# para imprimir el patron anterior usaremos un loop de 5 iteracciones con 
# impresiones de caharacteres multipliaccdo por el indici de la iteracion 
# se puede solicitar por consola el indice de la iterecion para hacer el loop 
# con ayuda del usuario que ejecuta el programa

i = int(input('Indique un numero del 1 al 10 para iterar un loop \n'))
for j in range (i+1): # un loop de i + 1 para no contar el 0
  print(str(j)*j) # convierto el entero a str y lo multiplico por la iteracion esa repite 
 # el caracter N cantidade veces

