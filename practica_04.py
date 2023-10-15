""" Write a program to remove characters from a string
 starting from zero up to n and return a new string. """
str = input('ingrese un string :\n')
indice = int(input('\nIngrese el indice que desea eliminar :\n'))

# str[2:] almacenara en str2 el string menos los 2 primeros caracteres
# str[:2] almacenara en str2 el string los 2 primeros caracteres
str2 = str[indice:] 
print("el nuevo string es: ",str2)

