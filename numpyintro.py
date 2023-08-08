import sys
import random
import re
import numpy as np

# Each import loads a "package" in Python, which is
# code that has been written for you to do common tasks
# In Computer Science, we call these APIs (application programming interface)
# This is fancy terminology for a pile of functions that do things
# Packages or APIs are a good idea, because they avoid reinventing the wheel

# Typical Data Science themed packages include:
# numpy, scikit-learn, TensorFlow, pandas, seaborn, matplotlib, pyTorch, ...
# There may be proprietary company APIs as well.

# numpy specifically is a package to support n-dimensional arrays natively
# Instead of 1 dimensional arrays, you might want to represent a grid (2D array)

# Create our first ndarray
a = np.zeros(5)
print(a)
print(type(a))
print(type(a[0]))

b = np.ones(10)
print(b)
print(b.shape)

b.shape = (1, 10)
print(b)
print(b.shape)

b.shape = (10,1)
print(b)
print(b.shape)

b.shape = (5, 2)
print(b)
print(b.shape)

# Cannot reshape an ndarray if you don't have enough data.
try:
    b.shape = (5, 3)
    print(b)
except:
    print("Cannot reshape an array if you don't have enough data!")
    
# Create the numbers from 1 to 10 having a total of 10 elements
z = np.linspace(1, 10, 10)
print(z)

# Create numbers from 2 to 10, with a total of 6 numbers
z = np.linspace(2, 10, 6)
print(z)

# Convert a traditional Python list into an ndarray
z = np.array([10, 20, 35])
print(z)
print(type(z[0]))

# Obviously, you can also do the conversion with a variable that is a list
a_list = [30, 42, 61]
z = np.array(a_list)
print(z)

# What about mismatched types?
# It will attempt to make all the types the same. If it can't, it 
# will scream or do something unexpected.
a_list = [12, 25, 'taco']
z = np.array(a_list)
print(z)
print(type(z[0]))

# Do this mismatching of list and value at your own risk
# This functionality is going away.
b_list = [12, 25, 'taco', [11, 13]]
z = np.array(b_list)
print(z)
print(z[3])
print(type(z[3]))

# Create a 2d ndarray from a 2d Python list. The list needs to be "regular"
# which means that it must make a full n x m matrix
c_list = [[1, 2, 3], [4, 5, 6]]
z = np.array(c_list)
print(z)

# Create a random numpy array (ndarray)
# Computers cannot create random numbers. We create something called pseudo-random
# numbers, which are generated from a pseudo-random number generator (PRNG). A PRNG
# takes a number as input (called a seed), which is used to create a specific sequence
# of "random-looking" numbers.
# As long as you give the PRNG the same seed, it will always generate the same numbers.
np.random.seed(37)
zrandomarray = np.random.randint(10, size=6)
print(zrandomarray)

# This is the first time we have used a seed when we were making random numbers.
# What does Python use for its seed if we don't tell it one?

print(zrandomarray[0:3])
print(type(zrandomarray[0:3]))
print(zrandomarray[-1])
print(type(zrandomarray[-1]))

