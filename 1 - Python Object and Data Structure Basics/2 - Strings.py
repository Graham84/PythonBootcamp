'''
Strings
Strings are used in Python to record text information, such as name. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).
This idea of a sequence is an important one in Python and we will touch upon it later on in the future.
In this lecture we'll learn about the following:
1.) Creating Strings
2.) Printing Strings
3.) Differences in Printing in Python 2 vs 3
4.) String Indexing and Slicing
5.) String Properties
6.) String Methods
7.) Print Formatting
'''

# Creating a String
# To create a string in Python you need to use either single quotes or double quotes. For example:

# Single word
a = 'hello'
print a

# Entire phrase
a = 'This is also a string'
print a


# We can also use double quote
a = "String built with double quotes"
print a

# Be careful with quotes!
# a ='I'm using single quotes, but will create an error'
# print a
# File "<ipython-input-4-6565b0b7b5e3>", line 2
# 'I'm using single quotes, but will create an error'
#    ^
# SyntaxError: invalid syntax
# The reason for the error above is because the single quote in I'm stopped the string.
# You can use combinations of double and single quotes to get the complete statement.
a = "Now I'm ready to use the single quotes inside a string!"
print a

# Printing a String
print 'Hello World'
print 'Hello World 1'
print 'Hello World 2'
print 'Use \n to print a new line'
print '\n'
print 'See what I mean?'
