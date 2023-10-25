"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. 
It should return true if the string is valid, and false if it's invalid.
This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], 
and curly braces {}. Thanks to @arnedag for the idea!
All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.



Escriba una función que tome una cadena de llaves y determine si el orden de las llaves es válido. 
Debería devolver true si la cadena es válida, y false si no lo es.
Esta kata es similar a la kata de paréntesis válidos, pero introduce nuevos caracteres: 
corchetes [] y llaves {}. Gracias a @arnedag por la idea.
Todas las cadenas de entrada serán no vacías, y sólo consistirán en paréntesis, corchetes y llaves: ()[]{}.

¿Qué se considera válido?
Una cadena de llaves se considera válida si todas las llaves coinciden con la llave correcta.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

"""