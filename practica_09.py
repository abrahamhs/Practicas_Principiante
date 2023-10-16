# Write a program to check if the given number is a palindrome number.
# para este ejercicio se me ocurre transformar todo a caracteres y hacer comaparacion


num = input('ingrese un numero : \n') # solicito el nuemro a evaluar
j = len(num) # Guardo en J el tamaño del string
x = 0        # x la inicio en 0 la utilizare para la iteracion del string
if j%2 == 0: # si J es multiplo de 2 
  x = j//2   # asigno a x la mitad del valor que toca iterar en el string Ej: 123456 x tendra 3
else:
  x = (j+1)//2 # Sumamos 1 si no es divisible para poder recorrer todo el string
  
counter = 0   # este contador lo uso para sumar cada iterecion que sea palindrome
for i in range (x): # Empezamos la Iteracion con la mitad del string
  comp1 = num[i] # asignamos a comp1 el caracter a evaluar segun el indice
  comp2 = num[j-i-1] # asignamos a comp2 el caracter a evaluar a la inversa
  if comp1 != comp2: # si no son iguales
    print('No es capicua') 
    break  # rompemos el loop y concluimos que no es un numero palindrome
  else:
    print(comp1,comp2) # caso contrario imprimimos el valor de cada caracter
    counter = counter + 1 # aumentamos el valor del contador 
if counter == x: print('Es capicua') # si la evaluacion de contador es igual el indice damos 
# por hecho que toda la cadena fue evaluada positivamente.

    
      
       
  
  