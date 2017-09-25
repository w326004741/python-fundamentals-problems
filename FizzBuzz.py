# FizzBuzz


# Using python range() function to create a list of numbers [0-99] so we can using  a for loop over it
for n in range(0,100):
    
    if n % 3 ==0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)