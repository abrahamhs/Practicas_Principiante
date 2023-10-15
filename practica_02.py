# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.
previous = 0  # declaro la variable en 0 para controlar cual es numero anterior
for i in range (10):  # creo una iteracion de i 10 veces
  # imprimo el valor de la iteracion, el valor de la variable que guardara en numero 
  # anterior de la iteracion y la suma de la iteracion actual con el valor de la iteracion anterior 
  print('El valos de la interacion es : ',
         i  ,' Numero anterior : ', previous ,'Suma: ', (i + previous) )
  # despues de imprimir todo, almaceno la iteracion actual para ser usada en el siguiente iteracion
  previous =  i  
