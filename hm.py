from random import randint
#importing the time module
import time

#welcoming the user
name = raw_input("What is your name? ")

print "Hello, " + name, "Time to play hangman!"

words = ["jumbo", "avengence", "importance", "desktop", "python", "premier", "product","power", "strength", "stronghold"]

value = randint(0, 9)
print(words[value])

guess = ''

for x in words[value]:
    guess += '-'

print(guess)

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero

    # print You Won        
print "You won"             

print

# ask the user go guess a character
guess = raw_input("guess a character:") 

# if the guess is not found in the secret word
if guess not in word:  

    # turns counter decreases with 1 (now 9)
    turns -= 1        

# print wrong
    print "Wrong"    

# how many turns are left
    print "You have", + turns, 'more guesses' 

# if the turns are equal to zero
    if turns == 0:           

    # print "You Lose"
        print "You Lose"