#Write a function that tests whether a string is a palindrome.


#define is used to declare the palindrome() function
def palindrome(word):
    palindrome_check = [] # make an empty list call palindrome_check
    
    # using for loop and the square bracke,there's three parameters that you can pass into a slice and third parameter is the order.
    # the list starting from the end.
    for c in word[::-1]:
        palindrome_check.append(c)
    print(palindrome_check)
    link = ''.join(palindrome_check)# using string.join to concatenate them all at the end.
    print(link)
    if link == word: # check the palindrome(word) string value whether or not palindrome.
        return True, print("This is a palindrome")
    else:
        print("This is NOT a palindrome")
palindrome("wnw")