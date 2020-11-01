from random import randint

name = input("what is your name?")

print("Hello, " + name + " , Time to play Hangman!")

words = ["jumbo", "avengence", "importance", "desktop", "python", "premier", "product","power", "strength", "stronghold"]

value = randint(0, 9)
print(words[value])

guess = ''

for x in words[value]:
    guess +=

print(guess)
