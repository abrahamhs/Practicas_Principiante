"""Write a program to accept a string from the user and display characters that are present
 at an even index number."""

str = input('Escriba una Palabra de mas de 6 letras\n')

if (len(str)>= 6 ):
  for i in range(0,len(str)):
    if (i%2==0):
      print(str[i])
