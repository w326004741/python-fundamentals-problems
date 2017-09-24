# FizzBuzz

for n in range(1,21):
    string = ""
    if n % 3 == 0:
        string = string + "Fizz"
    if n % 5 == 0:
        stirng = string + "Buzz"
    if n % 5 != 0 and n % 3 != 0:
        string = string  + str(n)
    print(string)