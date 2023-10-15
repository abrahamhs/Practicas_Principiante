"""Write a program to accept a string from the user and display characters that are present
 at an even index number."""

str = input('Escriba una Palabra de mas de 6 letras\n')

for i in range(0,len(str)): # se crea un loop con el tamaño del string
  if (i%2==0): # si el modulo del indice es 0 se imprime 
    print(str[i])
