import sys
import re
# import regex (which was "newly" released in 2020)
# is better in every way than re, but it is a private
# package owned by a company, so we will not use it

print("\t This means a tab.")
# To create a "raw" string that ignores escape symbols, prepend it with an r
print(r"\t This is a tab.")

# Regular expressions are a formalized "language" of templates
# to help you search for a pattern in a large document
# Pattern matching

multilinestring = '''
This is a multiline string.
I like tacos.
But tacos are expensive.
So I go to Taco Bell.
However, their tacos suck.
I, on the other hand, am amazing.
And definitely not a narcissist.
I have a mirror, but it doesn't reflect my personality.
You and I, on the other hand, have hands.
'''
multilinestring = multilinestring.strip()
print(multilinestring)
#print(multilinestring.split("\n"))

print()
# The ^ means "start of the line"
# Task: Find out how many times a line started with I.
for line in multilinestring.split("\n"):
    # Remove all leading and trailing whitespace
    line = line.strip()
    # re.search returns True if it finds it, False otherwise
    if re.search("^I", line):
        print("You are a narcissist.")

print()
# Count how many times taco appears in the string
tastycount = 0
for line in multilinestring.split("\n"):
    line = line.strip()
    if re.search('taco', line):
        tastycount += 1
print(tastycount)
