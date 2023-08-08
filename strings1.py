import sys
# This program teaches basics about strings

# Single or double quotes are the same.
fruit = 'bananas'
letter = fruit[1]
print(fruit, type(fruit))
print(letter, type(letter))

# functions on data types (like str) are called methods
# A method is a fancy name for a function for a built-in data type in Python
# One powerful method for a str is len
# len tells you the length of the strings
length = len(fruit)
print(length)

# Print the last letter of fruit
print(fruit[len(fruit)-1])
# Python way to do the same thing. . . .
print(fruit[-1])

# Print the last two letters of fruit
print(fruit[-2]+fruit[-1])

# Print that last letter seven times (F's in the chat for Roy)
print(fruit[-1]*7)

# C++ style
print()
index = 0
while index < len(fruit):
    print(fruit[index])
    index = index + 1
    
# Python way
print()
for i in fruit:
    print(i)
    
# Print the fruit in reversed form
print()
for i in reversed(fruit):
    print(i)
    
# Foreshadowing for next class!!!!
# Slices FTW!
print(fruit[::-1])