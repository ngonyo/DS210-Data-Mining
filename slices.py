import sys

# Slices are an excellent way to break up a string into parts.
# They work intuitively once you know the syntax.
s = 'syntaxes is for losers, bro'
print(s[0:6])
print(s[6:27])
print(s[6:len(s)])
print(s[6:]) # defaults to the end of the string
print(s[:6]) # default to the beginning of the string
print(s[:])

# The following two lines are identical
print(s[-1])
print(s[-1:])
# The following two lines are NOT the same
# The reason for this is that slices print every element in the range
print(s[-2])
print(s[-2:])

# More slicing, like Fruit Ninja but worse in every way
print(s[::-1]) # Produces the slice using the iterator of -1 (i.e. backwards)
print(s[::-2])
print(s[10:3:-3])