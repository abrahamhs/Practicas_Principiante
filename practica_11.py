# Write a Program to extract each digit from an integer in the reverse order.
 # For example, If the given int is 7536, the output shall be “6 3 5 7“, 
# with a space separating the digits.

#pido un numero cualquiera
num = int(input('Escribe una numero : \n')) #lo convierto a un entero en la variable num

numstr = str(num) # creo una segunda variable con num de tipo string
x = len(numstr) # le asigno a x el tamano de ese string con la funcion len()
list = [] # creo una lista vacia para agregar los caracteres 
while x > 0: # creo un bucle con el tamaño del string
  list.append(numstr[x-1])  # agrego cada caracter como numero en la lista
  x -= 1  # hago decrecer el contador del bucle
mystr = " ".join(list) # asigno a mystr el valos de la cadena invertido y con separaciones
print (mystr)



