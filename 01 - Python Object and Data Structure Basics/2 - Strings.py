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

# To use print function from Python 3 in Python 2
# from __future__ import print_function

print('Hello World')


# String Basics
# We can also use a function called len() to check the length of a string!

print len('Hello World')


# String Indexing
# We know strings are a sequence, which means Python can use indexes to call parts of the sequence.
# Let's learn how this works.
# In Python, we use brackets [] after an object to call its index.
# We should also note that indexing starts at 0 for Python.
# Let's create a new object called s and the walk through a few examples of indexing.

# Assign s as a string
s = 'Hello World'
print s
print (s)

# Let's start indexing!
# Show first element (in this case a letter)
print s[0]
print s[1]
print s[2]

#We can use a : to perform slicing which grabs everything up to a designated point.
# For example:
# Grab everything past the first term all the way to the length of s which is len(s)
print s[1:]
print

# Grab everything UP TO the 3rd index
print s[:3]

# Note the above slicing. Here we're telling Python to grab everything
# from 0 up to 3. It doesn't include the 3rd index.
# You'll notice this a lot in Python, where statements and are usually
# in the context of "up to, but not including".

# Everything
print s[:]

# Last letter (one index behind 0 so it loops back around)
print s[-1]

# Grab everything but the last letter
print s[:-1]


# We can also use index and slice notation to grab elements of a sequence by a
# specified step size (the default is 1). For instance we can use two colons in
# a row and then a number specifying the frequency to grab elements. For example:
print s
# Grab everything, but go in steps size of 1
print s[::1]
# Grab everything, but go in step sizes of 2
print s[::2]
# We can use this to print a string backwards
print s[::-1]


# String Properties
# Its important to note that strings have an important property known as
# immutability. This means that once a string is created, the elements within
# it can not be changed or replaced. For example
print s

# Let's try to change the first letter to 'x'
# s[0] = 'x'

# Traceback (most recent call last):
#   File "C:/Users/Graham/Desktop/Graham/CIT/git/PythonBootcamp/1 - Python Object and Data Structure Basics/2 - Strings.py", line 124, in <module>
#     s[0] = 'x'
# TypeError: 'str' object does not support item assignment

# Notice how the error tells us directly what we can't do, change the item assignment!
# Something we can do is concatenate strings!
# Concatenate strings!
print s + ' concatenate me!'

# We can reassign s completely though!
s = s + ' concatenate me!'
print s

# We can use the multiplication symbol to create repetition!
letter = 'g'
print letter*10



# Basic Built-in String methods
# Objects in Python usually have built-in methods. These methods are functions inside the object (we will learn about these in much more depth later) that can perform actions or commands on the object itself.
# We call methods with a period and then the method name. Methods are in the form:
# object.method(parameters)
# Where parameters are extra arguments we can pass into the method. Don't worry if the details don't make 100% sense right now. Later on we will be creating our own objects and functions!
# Here are some examples of built-in methods in strings:

# Upper Case a string
print s.upper()
# Lower case
print s.lower()
# Split a string by blank space (this is the default)
print s.split()
# Split by a specific element (doesn't include the element that was split on)
print s.split('W')

# There are many more methods than the ones covered here.
# Visit the advanced String section to find out more!

# Print Formatting
# We can use the .format() method to add formatted objects to printed string
# statements.
# The easiest way to show this is through an example:
print 'Insert another string with curly brackets: {}'.format('The inserted string')
