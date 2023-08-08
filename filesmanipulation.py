# Files are the bread and butter of data science.
# Most data is in a file, and you need to know how
# to read it.

# Some files, are stored in a specific manner called
# a csv, which is short form for comma separated values

s = 'spam,'
s = s * 8
print(s)
delimiter = ','
# The delimiter will tell us which character we will use
# to separate the string s
# the split method on a string separates the string at the
# position of the delimiter
t = s.split(delimiter)
t = s.split(",")
# The default delimiter for split is ' '
print(t)
print()

# Now we will deal with files in the same way
# Find out who sent me a message. We want to store the
# emails in a list so that we can spam them later.
# fhand is a "file handle", a data type like an int or a character
# but it is obviously more complicated
fhand = open('mbox-short.txt')
emaillist = []
for line in fhand:
    # Strip trailing whitespace characters from the line
    line = line.rstrip()
    if not line.startswith('From'):
        continue # continue will skip the rest of the iteration and start the loop again
    # Now that I'm here, I know that line starts with From:
    email = line.split()
    print(email)
    emaillist.append(email[1])
print(emaillist)

# Exercise 1
# I want to know the length of a person's username
totaluserlength = 0
for email in emaillist:
    position = email.find('@')
    totaluserlength += position
    print(position, totaluserlength)
print(totaluserlength)

# Exercise 2
# Remove duplicates from the emaillist
uniqueemaillist = []
for email in emaillist:
#    if not email in uniqueemaillist: This the same as the one below
    if email not in uniqueemaillist:
        uniqueemaillist.append(email)
print(uniqueemaillist)

# Exercise 3
# Counts the username length total among the unique list
totaluserlength = 0
for email in uniqueemaillist:
    position = email.find('@')
    totaluserlength += position
    print(position, totaluserlength)
print(totaluserlength)

# Strings also can check what they end with, using the method endswith("whatever")