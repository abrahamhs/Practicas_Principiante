# kata_01 Stop gninnipS My sdroW!
""" Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words
 reversed (Just like the name of this Kata). Strings passed in will 
 consist of only letters and spaces. Spaces will be included only 
 when more than one word is present."""

def spin_words(sentence):
    str = sentence.split() # divido la oracion en palabras
    str_temp = [] # creo una lista vacia para almacenar las palabras
    for i in str: # itero las palabras
        if len(i) >= 5: 
            str_temp.append(i[::-1])  # palabra que hay que girar
        elif len(i) < 5:
            str_temp.append(i) # palabra sin girar
    mystr = " ".join(str_temp) # unos cada palabra de la lista con espacio
    return mystr
# Test cases
test_Str = input('Introduce un Comentario \n\n')
print(f'\n{spin_words(test_Str)}\n')