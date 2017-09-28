#factorial-digit-sum    -by Weichen Wang

#define is used to declare the factorial() function
def factorial(n):
    # 0 of factorial equal to 1
    if n == 0:
        return(1)
    # 0 of factorial equal to 1
    elif n == 1:
        return(1)
    #In addition to 0 and 1, other factorial value is n*factorial(n-1)
    else:
        return(n*factorial(n-1))
# define is used to declare the main() function
def main():
    #set x value is 100
    x = 100
    answer = factorial(x)
    #using list and string to show the factorial(100)
    digits = list(str(answer))
    #using for() loop print out sum of digits
    sum_of_digits = 0
    for digit in digits:
        sum_of_digits += int(digit)
    print(sum_of_digits)
main()
