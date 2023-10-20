""" Se le da una matriz (que tendrá una longitud de al menos 3, 
pero podría ser muy grande) que contiene números enteros. 
La matriz estára toda compuesta  por enteros impares o  por enteros pares
con excepcion por un único entero N en la matriz de los pares este sera impar
en la matriz de los impares este sera par. 
Escriba un método que tome la matriz como argumento y devuelva este "valor atípico" de N.
Ejemplos:
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
"""
def find_outlier(matriz):
    # variable de control
    par = 0
    impar = 0
    cont = 0
    n = []
    # verifico si el array tiene mas de 3 elementos para proceder a verificarlo e caso contrario retorno None
    if len(matriz) < 3:
        return None
    else:
        # aqui compruebo si es un array mayormente impar o par
        for i in range(len(matriz)):
            if matriz[i] % 2 == 0:
                par += 1   # sumo los nuemros pares del array
            else:
                impar += 1 # sumo los numeros impares del array
    # valido si voy a trabajar un array par
    if par > impar:
        for j in range(len(matriz)): # recorro la matriz
            if matriz[j] % 2 != 0:  # valido cual es ese numero que no es par
                n = matriz[j] # procedo a guardarlo
                cont +=1  # contador de control para verificar que solo se dara el resultado si hay un solo numero impar
        if cont == 1: # si al final de recorrer la matriz el contador es igual a 1 retorno n que tiene el valor de ese N impar
            return print(f'{n} el unico numero par')
        else:
            return None   # si el contador supera 1 retorno None
    # si no es un array para es impar    
    else:
        for j in range(len(matriz)):  # igual que el procesado de los pares pero para matrices impares
            if matriz[j] % 2 != 1:
                n = matriz[j]
                cont += 1
        if cont == 1:
            return print(f'{n} el unico numero impar')
        else:
            return None
       
# Test
buscar_atipico = [2, 4, 0, 100, 4, 11, 2602, 36] 
find_outlier(buscar_atipico)
buscar_atipico = [160, 3, 1719, 19, 11, 13, -21]
find_outlier(buscar_atipico)      