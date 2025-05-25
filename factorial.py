#assigment one:find the factorial of a number (five):
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
print (factorial(5)) 