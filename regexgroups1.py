import sys
import re

# Introduction to RegEx Groups
# A regex group, denoted by (), encloses a portion of the pattern that you
# want to match
# This allows you "capture" only the part of the match that you really want.
# So, you can use the entire pattern to get to the right kind of information
# and only SAVE the subset of that match that really matters to you.

# Exercise 3 (now with 100% more groups)
fhand = open('regexdata.txt')
contents = fhand.read()
zipcodes = re.findall(r'(\d{5})\n', contents) # enclose the digits in a regex group
print(len(zipcodes))
print(zipcodes)
zipcount = {}
for z in zipcodes:
    if z not in zipcount:
        zipcount[z] = 1
    else:
        zipcount[z] += 1
print(zipcount)
fhand.close()

# Exercise 4
# Calculate how many people are in each zip code
# Calculate how many people are in each state
fhand = open('regexdata.txt')
contents = fhand.read()
# statezip = re.findall(r'(\w{2}) (\d{5})\n', contents)
statezip = re.findall(r'([A-Z]{2}) (\d{5})\n', contents)
print(statezip)
statezipnum = []
for sz in statezip:
    sz = (sz[0], int(sz[1]))
    statezipnum.append(sz)
print(statezipnum)

# Alternate way to do the same numeric conversion task
statezipnum = []
for s, z in statezip:
    statezipnum.append((s,int(z)))
print(statezipnum)

count = {}
for s, z in statezipnum:
    if z not in count:
        count[z] = 1
    else:
        count[z] += 1
    if s not in count:
        count[s] = 1
    else:
        count[s] += 1
print(count)

fhand.close()

