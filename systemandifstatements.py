import sys

# This is a comment.
"""
This is comment line 1.
This is comment line 2.
"""

# The default type of any input is a string or 'str'
n = int(input())
"""
These lines makes it more clear what you are doing.
n = input()
n = int(n)
"""

if (n > 4):
    print("Hello")
    print("Your number is larger than 4.")
else:
    print("Your number is less than or equal to 4.")
    
# Command line parameters
# A command line parameter is the stuff you put after
# your python script name that is built-in input to your
# program.

print(sys.argv[0])
if (len(sys.argv) >= 2):
    print("I want to eat", sys.argv[1])
else:
    print("You are clearly not hungry.")
    
# Complex if statements and boolean expressions

x = int(input("What is your favorite number? "))
if x < 5:
    print("You dream too small.\nGo away.")
elif x == 7:
    print("Lucky numba 7.")
elif x < 29:
    print("Still dating age.")
elif x >= 40 and x < 59:
# C++ used && or ||. This is SO MUCH BETTER.
    print("Third time's the charm.")
elif x != 69:
    print("You missed the best number.")
else:
    print("Just die already.")