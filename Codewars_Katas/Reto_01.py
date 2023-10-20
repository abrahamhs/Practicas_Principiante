# kata_01 Stop gninnipS My sdroW!
""" Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words
 reversed (Just like the name of this Kata). Strings passed in will 
 consist of only letters and spaces. Spaces will be included only 
 when more than one word is present."""

def spin_words(sentence):
    str = sentence.split()
    str_temp = []
    for i in str:
        if len(i) >= 5:
            str_temp.append(i[::-1])
        elif len(i) < 5:
            str_temp.append(i)
    mystr = " ".join(str_temp)
    return mystr
test_Str = input('Introduce un Comentario \n\n')
print(f'\n{spin_words(test_Str)}\n')