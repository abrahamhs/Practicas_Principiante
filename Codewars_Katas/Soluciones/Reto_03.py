# Persistent Bugger nivel < 6kyu >
""" 
Write a function, persistence, that takes in a positive parameter num and 
returns its multiplicative persistence, which is the number of times you 
must multiply the digits in num until you reach a single digit.

Escribe una función, persistencia, que reciba un parámetro positivo num
y devuelva su persistencia multiplicativa, que es el número de veces que 
debes multiplicar los dígitos de num hasta llegar a un solo dígito.

Ejemplo:
 
    39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
    999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
    4 --> 0 (because 4 is already a one-digit number)
 
 
 """

def persistence(n):
    # Validamos que n no sea de tipo float para poder calcular su persistencia
    if type(n) == float:
        return None
    # Verificamos si el numero es positivo
    if type(n) == int:
        if n < 0:
            return None
        
        # Si el número es de un solo dígito, su persistencia es 0
        elif len(str(n)) == 1:
            return 0
        
        # Si el número tiene más de un dígito, procedemos a calcular su persistencia
        elif len(str(n)) > 1:
            
            # Creamos una lista para almacenar los dígitos y la llenamos en un bucle
            # Usamos un bucle for para llenar la lista a partir de los caracteres de n 
            lista = []
            for i in str(n):
                lista.append(int(i))
                
            # Inicializamos una variable para operar las multiplicaciones y obtener su nuevo valor
            resultado  = 0 
            # Inicializamos un contador de iteraciones
            contador = 0

            ###########################################################################
            #### Si quieres ver que pasa en cada itereacion descomenta los printf######
            ###########################################################################
            
            # print(f'El valor de list es:. {lista}')
            # print(f'su tamaño es de: {len(lista)} digitos')

            # Creamos un bucle que se ejecuta hasta que la lista tenga un solo dígito
            while len(lista) > 1:
                
                # Aumentamos el contador por cada iteración
                contador += 1 

                # Asignamos el valor del primer número de la lista como valor inicial
                # de la multiplicacion de sus digitos.
                resultado  = lista[0] 
                
                # Creamos un bucle que se ejecuta por cada número que tenga en la lista
                # a partir de la posicion 1 ya que la posicion 0 la hemos usado anteriormente
                for i in range(1, len(lista)):
                    resultado  *= lista[i]
                
                # Convertimos el resultado en una cadena para descomponerlo en dígitos    
                my_str = str(resultado )

                # Almacenamos los dígitos del resultado en la lista nuevamente.
                lista = [int(i) for i in my_str]
                
                # print(f'El valor de list es:. {lista}')
            

            # Retornamos el contador de iteraciones, que representa la persistencia
            # print(contador)
            return contador
            
            
            


print(persistence(4))