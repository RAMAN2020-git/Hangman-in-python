from random import randint

name = input("what is your name?")

print("Hello, " + name + " , Time to play Hangman!")

words = ["jumbo", "avengence", "importance", "desktop", "python", "premier", "product","power", "strength", "stronghold"]

value = randint(0, 9)
print(words[value])

secret = words[value]

guess = ''

for x in words[value]:
    guess += '-'

print(guess)
while(True):
    letter = input("Guess a letter?")

    new_guess = ''
    for x in range(len(secret)):
        if (secret[x] == letter):
            new_guess += letter
        elif (secret[x] == guess[x]):
            new_guess += secret[x]
        else:
            new_guess += '-'
    guess = new_guess

    print(guess)