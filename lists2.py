import sys

# List methods
t = ['e', 'd', 'c', 'b', 'a']
print(t)
t.append('f')
print(t)

# Using append with an empty list allows you to build a list

t2 = ['h', 'g']
t.extend(t2)
print(t)

# This is how you sort a list
t.sort()
print(t)

# the pop method removes an item from list t at a specified index value 
# and returns it
# By default, pop removes the last element of the list
popped = t.pop(1)
print(popped, t)
t.pop()
print(t)

# Another way to "pop" an element of a list without a return value
# This method is not very "pythonny"
# One advantage is that it lets you pop "slices" of lists, which is why
# you might see it being used
del t[1:3]
print(t)

# Remove allows you to get rid of an element by its name
# It removes only one copy of the element requested
# Can only remove elements in the list
print()
t = ['e', 'd', 'c', 'b', 'a', 'g', 'h', 'j', 'e']
print(t)
t.sort()
t.remove('e')
print(t)
if ('w' in t):
    t.remove('w')

# Specific methods for numeric lists only
numlist = [-45, 1, 2, 3, 4, 5, 9001, 54]
print(numlist)
print(max(numlist))
print(min(numlist))
print(sum(numlist))

# Two ways to create an empty list
empty = []
empty = list()