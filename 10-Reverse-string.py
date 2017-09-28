# Write a function to reverse a string.
# by Weichen Wang


user_input = input('Enter your text: ')

word = str(user_input)

#using define len() to show the lenght of your enter text
lenght = len(word)

i = lenght

# set a empty list for final
final = []

while i > 0:
    # append n to the final array
    final.append(word[i-1])
    # each time keep decreasing
    i -= 1
    # using the join() method
reversed = ''.join(final)

print(reversed)