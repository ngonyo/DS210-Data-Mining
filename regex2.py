import sys
import re
# import regex (which was "newly" released in 2020)
# is better in every way than re, but it is a private
# package owned by a company, so we will not use it

phone_numbers = '''
321-555-4321
123-555-1234
123*555*1234
800-555-1234
900-867-5309
888&456&7654
8884456k7654
'''

billionare_money = '''
60,000,000,000.21
34,000,000.98
120,000,000,000.32
3,000,000,000.33
3,000.00
3,,,123.16
456,123,678,111,231.34
'''

# The re package creates and uses something called a match object, which is
# internal to the re package. For the sake of this class, we will avoid using
# match objects as much as possible.
testthis = re.search('555', phone_numbers)
print(testthis)

# The finditer method creates a "list" of match objects that stores all matches
testthis = re.finditer('555', phone_numbers)
print(testthis)
for x in testthis:
    print(x)
    
print()
# The findall function is the one we will use most often
# findall creates a normal list of all matches for the pattern you searched for
testthis = re.findall('555', phone_numbers)
print(testthis)

print()
# Find all phone numbers that are correctly formatted 
testthis = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', phone_numbers)
print(testthis)

# Indonesia uses the * symbol as a separator between digits in
# its phone numbers. (This is straight lies, btw.) Then, the *
# phone number is also valid.
testthis = re.findall(r'\d\d\d[*-]\d\d\d[*-]\d\d\d\d', phone_numbers)
print(testthis)

# Implement International Awareness of Other Countries Day
testthis = re.findall(r'\d\d\d.\d\d\d.\d\d\d\d', phone_numbers)
print(testthis)

# I want to find all "phone numbers" that are not - or & separated.
testthis = re.findall(r'\d\d\d[^-&]\d\d\d[^-&]\d\d\d\d', phone_numbers)
print(testthis)

# I want to find all "phone numbers" that are not - or & separated.
# Use a fixed value quantifier to match the string
# A quantifier specifies how many times a particular subpattern is desired.
# You can search for a specific number of times, or "at least" kinds of amounts
# You can also search for a specific range of number of times.
testthis = re.findall(r'\d{3}[^-&]\d{3}[^-&]\d{4}', phone_numbers)
print(testthis)

# Find all the billionaires.
testthis = re.findall(r'\d{1,3}(?:,\d{3}){3,}[.]\d{2}', billionare_money)
print(testthis)

names = '''
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr. cummings
'''

# Exercise 1
# Output the names of every male on this list.
males = re.findall(r'Mr\.? ', names)
print(males)

# The above code gets the prefix of the person's name right.
# But the name isn't there!!!!
males = re.findall(r'Mr\.? \w+', names)
print(males)

# Sometimes you want letters from a specific set of characters.
# You represent a set with [].
males = re.findall(r'Mr\.? [A-Z][a-z]*', names)
print(males)

# We want to find every name that starts with S or T.
stnames = re.findall(r'M\w+[.]? [S|T|F|U][a-z]*', names)
print(stnames)

stnames = re.findall(r'M\w+[.]? (?:S|T|F|U)[a-z]*', names)
print(stnames)

# Exercise 2 (project 2 practice!!!!)
# Output all the phone numbers from regexdata.txt
fhand = open('regexdata.txt')
contents = fhand.read()
print(type(contents))
print(len(contents))
phnum = re.findall(r'\d{3}-\d{3}-\d{4}', contents)
print(phnum)
print(len(phnum))

# Exercise 3
# Report how many people live in each zip code.
fhand = open('regexdata.txt')
contents = fhand.read()
zipcodes = re.findall(r'\d{5}\n', contents)
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
# Checking your code to make sure that it gives you the answer
# that you expect is called "testing"

# For example, we didn't like that our zip codes come with a \n also