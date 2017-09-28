# Write a guessing game where the user must guess a secret number -by Weichen Wang
#Step 1: Computer pick a random number
#Step 2: Player make a guess
#Step 3: Compare guess to the number
#Step 4: Print out "Too High","Too Low","You got it"
import random #import random libray to use the random number function

secret = random.randrange(1,101)#把随机数（1，101）赋值给secret
#print(secret) 

guess = 0 # set guess initial value or start value that the program begin has something to compare
tries = 0 # set try times initial value
while guess != secret:
    guess = int(input("Make a guess: ")) # Player make a guess
    tries = tries + 1 # Record the number of time of tries 

    if guess > secret: #If player guess the number is greater than secret,than print out Too High
        print("Too High!")
    elif guess < secret: #If player guess the number is less than secret,than print out Too Low
            print("Too Low!")
    else:  #If player guess the number is equal to secret,than print out You got it
            print("You got it!!")

print("Number of tries: ", tries)