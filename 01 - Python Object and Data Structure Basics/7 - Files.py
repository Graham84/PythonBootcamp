# Files
'''
Python uses file objects to interact with external files on your computer.
These file objects can be any sort of file you have on your computer, whether it be an audio file,
a text file, emails, Excel documents, etc. Note: You will probably need to install certain libraries
or modules to interact with those various file types, but they are easily available.
(We will cover downloading modules later on in the course).
Python has a built-in open function that allows us to open and play with basic file types.
First we will need a file though. We're going to use some iPython magic to create a text file!
'''



# Python Opening a file
# We can open a file with the open() function. The open function also takes in arguments (also called parameters). Lets see how this is used:

# Open the text.txt we made earlier
f = open('test.txt')

# We can now read the file
print f.read()
# This is a new line

# But what happens if we try to read it again?
print f.read()
#

# This happens because you can imagine the reading "cursor" is at the end of the file after having read it.
# So there is nothing left to read. We can reset the "cursor" like this:

# Seek to the start of file (index 0)
f.seek(0)

# Now read again
print f.read()
# # This is a new line
# In order to not have to reset every time, we can also use the readlines method.
# Use caution with large files, since everything will be held in memory.
# We will learn how to iterate over large files later in the course.
f.seek(0)
# Readlines returns a list of the lines in the file.
print f.readlines()
# ['This is a new line']

# Writing to a File
# By default, using the open() function will only allow us to read the file, we need to pass the argument 'w' to write over the file. For example:

# Add a second argument to the function, 'w' which stands for write
my_file = open('test.txt', 'w+')

# Write to the file
my_file.write('This is a new line')

# Read the file
print my_file.read()

# 'This is a new line'
# Iterating through a File
# Lets get a quick preview of a for loop by iterating over a text file. First let's make a new text file with some iPython Magic:


# Now we can use a little bit of flow to tell the program to for through every line of the file and do something:

for line in open('test.txt'):
   print line


# Don't worry about fully understanding this yet, for loops are coming up soon. But we'll break down what we did above. We said that for every line in this text file, go ahead and print that line. Its important to note a few things here:
# 1.) We could have called the 'line' object anything (see example below).
# 2.) By not calling .read() on the file, the whole text file was not stored in memory.
# 3.) Notice the indent on the second line for print. This whitespace is required in Python.

# We'll learn a lot more about this later, but up next: Sets and Booleans!

# Pertaining to the first point above
#for asdf in open('test.txt'):
 #   print asdf
# First Line

# Second Line