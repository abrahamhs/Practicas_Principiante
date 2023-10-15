# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.
previous = 0
for i in range (10):
  print('El valos de la interacion es : ', i  ,' Numero anterior : ', previous ,'Suma: ', (i + previous) )
  previous =  i
