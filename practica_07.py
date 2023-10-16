# Write a program to find how many times substring “Emma” appears in the given string.
str_x = "Emma is good developer. Emma is a writer"
# output : Emma appeared 2 times

""" def count_substring(string, sub):
      return len([i for i in range(len(string)) if string[i:].startswith(sub)])
    print(f'Emma appeared {count_substring(str_x,"Emma")} times')
 """
# Usaremos en metodo count() cuya sintaxis es string.count(caracteres) o 
# string.count(caracteres, int(inicio). int(final))
# El metodo count() devuelve la cantidad de veces que el carácter/s se repite en una cadena de text
print(f'Emma appeared {str_x.count("Emma")} time') # Solución con método count().