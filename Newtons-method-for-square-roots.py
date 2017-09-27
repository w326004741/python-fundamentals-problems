# Implement the square root function using Newton's method. In this case, Newton's method is to approximate sqrt(x) by picking a starting point z and then repeating:
# z_next = z - ((z*z - x) / (2 * z)).
# by Weichen Wang

def f(x):
    # define is used to declare the f(x) function and return any eqution just you like.
    return 9 - x*(x-10)


def fprime(x): 
    # define is used to declare the fprime(x) function and return derivative of the f(x) funtion eqution
    return -2*x + 10

guess = -10 # set guess inital value

for val in range(1,11):
    # just like  z_next = z - ((z*x - x) / (2 * z))
    nextGuess = guess - f(guess)/fprime(guess)
    print(nextGuess)
    # last nextGuess value assigned to next guess to figure out next nextGuess value.
    guess = nextGuess