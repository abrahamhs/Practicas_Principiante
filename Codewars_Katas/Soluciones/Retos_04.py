# Convert string to camel case
"""
Complete the method/function so that it converts dash/underscore 
delimited words into camel casing. The first word within the output 
should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case). 
The next words should be always capitalized.

Complete el método/función para que convierta las palabras 
delimitadas por guiones/guiones bajos en mayúsculas y minúsculas. 
La primera palabra de la salida debe ir en mayúsculas sólo si la 
palabra original iba en mayúsculas (lo que se conoce como 
Mayúsculas Camel Case, también conocido como Pascal case). Las palabras 
siguientes deben ir siempre en mayuscula

Ejemplos:

"the-stealth-warrior" --->  "theStealthWarrior"

"The_Stealth_Warrior" ---> "TheStealthWarrior"

"The_Stealth-Warrior" ---> "TheStealthWarrior"

"""


# Defino el nombre de la función
import re

def to_camel_case(text):
    # Comprobamos si la cadena de texto es vacía
    if not text:
        text += ''  # Si es vacía, la dejamos como está y la retornamos
        return text
    
    # Usamos la librería 're' para reemplazar guiones y guiones bajos por espacios
    palabra_1 = re.sub('[-_]', " ", text)

    # Usamos split() para dividir la cadena en palabras
    palabra_2 = palabra_1.split()

    # Inicializamos la variable donde guardaremos el resultado en formato CamelCase
    palabra_camelCase = palabra_2[0]
    
    # Recorremos las palabras a partir de la segunda y las capitalizamos
    for i in range(1, len(palabra_2)):
        palabra_camelCase += palabra_2[i].capitalize()

    # Imprimimos el resultado para visualizarlo
    print(palabra_camelCase)
    
    # Retornamos el resultado en formato CamelCase
    return palabra_camelCase

# Ejemplos de uso de la función
to_camel_case("the-stealth-warrior")  # Debe imprimir "theStealthWarrior"
to_camel_case("The_Stealth_Warrior")   # Debe imprimir "TheStealthWarrior"
to_camel_case("The_Stealth-Warrior")   # Debe imprimir "TheStealthWarrior"



# Post    Se entiende mejor como se desarrolla el código :-)
