import sys

# Explicitly defined strings in Python are immutable
# Immutable means that they cannot be changed!
greetings = 'Welcome to Monday!'
# greetings[0] = 'H'

# Strings are a very powerful data type, and there are
# a lot of functions written for it already. How do you
# know what is already available for you to use?
# print(dir(greetings))
# print(type(greetings))
# print(help(str.capitalize))

# Exercise
# The user will type in a string and a letter.
# You have to write a program that finds out if the letter is in the string.
phrase = input("Tell me a phrase, bro. ")
letter = input("Letter me. ")

# Does the letter appear in the phrase?
for x in range(len(phrase)):
    if letter == phrase[x]:
        print("I got you, bro.")
        
# C++ style (with explicit index values)
# How many times does letter appear in the phrase?
print()
count = 0
for x in range(len(phrase)):
    if letter == phrase[x]:
        count = count + 1
print(count)
        
# Python method
print()
count = 0
for x in phrase:
    if letter == x:
        count += 1
print(count)