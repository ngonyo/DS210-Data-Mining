'''
A dictionary is like a list. In fact, it's almost
the "same" as a list, except for one tiny detail:
the index value of a dictionary can be ANYTHING.

"Under the hood" a dictionary is actually a hash
table data structure, and it is very powerful!

A data structure is an "object" that contains data
inside of it in a specific way that makes accessing
that data somehow faster or better or uses less space.
You know about arrays already, which are one kind of 
data structure.

The index of a dictionary is called a "key"
The element at that key is commonly called a "value"
'''

# Let's get dict()
l33t2eng = dict()
l33t2eng = {}
print(l33t2eng)

l33t2eng['fox'] = 'good lookin\' person'
print(l33t2eng)

# Explicit declaration of a dictionary
l33t2eng = {'scroogin':'break up to save money', 
            'n00b': 'new player',
            'suxxors': 'you suck',
            'git gud': 'get good',
            'rigged': 'i didn\'t win'}
print(l33t2eng)

# Many things work for dictionaries. You can find
# details using the help menu or the internet.
print(len(l33t2eng))

# Boolean expressions
# tell you if something is there as a KEY in the dictionary
print('n00b' in l33t2eng)
print('get good' in l33t2eng)
print(l33t2eng['n00b'])

# Unlike a list. . . 
# for x in list
# makes x equal to elements (or values) of a list 
# similar code for dictionaries makes x the KEY
# In other words, dictionaries have to be indexed like arrays
# in C++
for key in l33t2eng:
    print(key, l33t2eng[key])

# Exercise 
# Find out how many of each letter there are in the following string
words = "supercalifragilisticexpallidocious paraskivadecatriaphobia"
# a -- 4
# b -- 3
# ...
# z -- 0
lettercount = {}
# lettercount is going to be a dictionary that is indexed
# by a letter (instead of a number) and its value will be
# how many times that letter appears in the string
for letter in words:
    if letter in lettercount:
        lettercount[letter] += 1
    else:
        lettercount[letter] = 1
        
for letter in lettercount:
    print(letter, lettercount[letter])
    
# 12.5% eighth-theist joke
# dict.keys() returns a tuple (of size 1) with a list of keys inside.
# A tuple is an immutable list. It is identified by using parenthesis.
# For example, (4, 6) is a tuple. 
# The code below extracts the list as a keylist:
keytuple = lettercount.keys()
print(keytuple)
keylist = list(lettercount.keys())
print(keylist)
keylist.sort()
print(keylist)

for letter in keylist:
    print(letter, lettercount[letter])

