import sys

'''
Exception handling is a programming language construct that
takes care of erroneous or non-matching data in an elegant way
so that the program does not crash
'''

temperature = input("Enter the current temperature (in F). ")
try:
    # This mechanism converts one type into another (in this case, float)
    fahr = float(temperature)
    celsius = (fahr - 32) * (5/9)
    print(celsius)
except:
    print("You dumb. You entered", temperature, "which is dumb.")
  