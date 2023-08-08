import sys

c = [10, 20, 30, 40]
d = ['taco', 'burrito', 'cat', 'frog']
print(c)
print(d)

listception = [c, d, d]
print(listception)

listlistception = [listception, listception]
print(listlistception)
listlistlistception = [listlistception]
print(listlistlistception)

# Lists do not have to have the same type of thing in each position
wtf = ['spam', [2], 7.5, listception]
print(wtf)
print(type(wtf))

emptylist = []
print(emptylist)

print()
print(c[0])

# Unlike strings, lists are mutable. So you can change any part of them
# that you want.
c[1] = "orange"
print(c)

# If you try to access a list element that is off the edge, it will error out.
# print(c[4])

# Boolean operations on lists (boolean operators are either true or false)
print(5 in wtf)
print(2 in wtf)
print([2] in wtf)
print([c, d, d] in wtf)

print()
# How to print the contents of a list
for x in c:
    print(x)
    
print()
for x in range(len(d)):
    print(d[x])
    
# range is a function that actually creates a *list*, not a set like I said
# earlier. In other words, "x in range(5)" is really a boolean operation
# on the list [0, 1, 2, 3, 4]

# This loop executes 0 times!
for x in []:
    print("Hi")
    
print('-'*10)

# List concatenation (IMPORTANT!)
biglist = [1, 2] + [3, 'random']
print(biglist)
print([1, 2, 3] * 4)

# What about slices?
print(c[:])
print(c[::-1])

# Le Le Shaniqua
name = "Shaniqua"
print("le" + " le " + name)



