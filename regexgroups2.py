import sys
import re

# A different way to refer to groups!
fhand = open('regexdata.txt')
contents = fhand.read()
regioninfo = re.finditer(r'([A-Z]{2}) (\d{5})\n', contents)
print(regioninfo)
states = {}
for instance in regioninfo:
#    print(type(instance))
#    print(instance)
    if instance.group(1) not in states:
        states[instance.group(1)] = 1
    else:
        states[instance.group(1)] += 1
print(states)
fhand.close()

# Find only zip codes from IN or VA
fhand = open('regexdata.txt')
contents = fhand.read()
localinfo = re.findall(r'(IN|VA) (\d{5})\n', contents)
print(localinfo)
fhand.close()

# Find the first names of anyone whose last name is Arnold.
fhand = open('regexdata.txt')
contents = fhand.read()
arnoldinfo = re.findall(r'([A-Z][a-z]*) Arnold\n', contents)
print(arnoldinfo)
fhand.close()