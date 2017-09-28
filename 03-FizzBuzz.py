# FizzBuzz- by Weichen Wang


# Using python range() function to create a list of numbers [0-99] so we can using  a for loop over it
for n in range(0,100):
    # if the index is a multiple 3 and the index is a multiple 5, then print out "FizzBuzz"
    if n % 3 ==0 and n % 5 == 0:
        print("FizzBuzz")
    # if the index is a multiple 3, then print out "Fizz"
    elif n % 3 == 0:
        print("Fizz")
    # if the index is a multiple 5, then print out "Buzz"    
    elif n % 5 == 0:
        print("Buzz")
    # if the index is not a multiple or 3 and 5 or 3 or 5,then just print out index
    else:
        print(n)