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
import re

# Defino el nombre de la funcion
def to_camel_case(text):
    # la linea de codigo siguiente depende de la libreria (re) que hay que importar
    # busca [-_], remplaza por " ", en la cadena: text
    palabra_1 = re.sub('[-_]'," ",text)

    # split() divide una cadena en una lista de cadenas basada en un separador
    palabra_2 = palabra_1.split()

    # creo una lista que devolvere y asigno lo que esta en palabra_2 en el indice 0
    palabra_camelCase = palabra_2[0]
    
    # cre un loop que recorrera la lista desde la posicion 1 hasta el tamaño 
    # de la lista dado por la funcion len() con esto evito iterar con el contenido
    # del indice 0 y asi obtengo lo deseado
    for i in range(1, len(palabra_2)):
        palabra_camelCase += palabra_2[i].capitalize()
        
    # imprimo para visualizar el resultado 
    print(palabra_camelCase)
    
    # retorno el resultado
    return palabra_camelCase

to_camel_case("the-stealth-warrior")
to_camel_case("The_Stealth_Warrior")
to_camel_case("The_Stealth-Warrior")
