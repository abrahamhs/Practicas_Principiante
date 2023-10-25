# Split Strings  nivel < 6kyu >

"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing 
second character of the final pair with an underscore ('_').

Complete la solución para que divida la cadena en pares de dos caracteres. 
Si la cadena contiene un número impar de caracteres, debe sustituir el segundo carácter 
que falta del último par por un guión bajo ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

"""

def solution(s):
    # Verificamos si la longitud de la cadena es impar.
    if len(s) % 2 == 1:
        # Si es impar, agregamos un guion bajo al final de la cadena.
        s += '_'
        
    # Dividimos la cadena en pares y la almacenamos en una lista llamada 'par'.
    par = [s[i : i + 2] for i in range(0, len(s), 2)]

    # Imprimimos la lista de pares de caracteres.
    print(par)

    # Retornamos la lista de pares.
    return par

# Ejemplo de uso de la función con la cadena 'abcdfghjstfrdhs'
solution('abcdfghjstfrdhs')

    