# Decorators
# Decorators can be thought of as functions which modify the
# functionality of another function.
# They help to make your code shorter and more "Pythonic".
# To properly explain decorators we will slowly build up from
# functions. Make sure to restart the Python and the Notebooks
# for this lecture to look the same on your own computer.
# So lets break down the steps:


# Functions Review
def func():
    return 1

print func()


# Scope Review
# Remember from the nested statements lecture that Python
# uses Scope to know what a label is referring to. For example:

s = 'Global Variable'

def func():
    print locals()

# Remember that Python functions create a new scope, meaning
# the function has its own namespace to find variable names
# when they are mentioned within the function.
# We can check for local variables and global variables
# with the local() and globals() functions. For example:

print globals()
# {'__builtins__': <module '__builtin__' (built-in)>,
#  '__file__': 'C:/Users/Graham/Desktop/Graham/CIT/git/PythonBootcamp/11 - Decorators/1 - Part 1.py',
#  '__package__': None, 's': 'Global Variable',
#  'func': <function func at 0x024B28F0>,
#  '__name__': '__main__', '__doc__': None}

print globals().keys()
# ['__builtins__', '__file__', '__package__', 's',
#  'func', '__name__', '__doc__']

print globals()['s']
# Global Variable

# Now lets run our function to check for any local variables
# in the func() (there shouldn't be any)

print func()
# {}

# Great! Now lets continue with building out the logic of what
# a decorator is. Remember that in Python everything is an object.
# That means functions are objects which can be assigned labels
# and passed into other functions. Lets start with some simple
# examples:

def hello(name = 'Graham'):
    return 'Hello ' + name

print hello()
# Hello Graham

# Assign a label to the function. Note that we are not using
# parentheses here because we are not calling the function hello,
# instead we are just putting it into the greet variable.

greet = hello
print greet
# <function hello at 0x023F2930>

print greet()
# Hello Graham

# This assignment is not attached to the original function:

del hello
# print hello()

# Traceback (most recent call last):
#   File "C:/Users/Graham/Desktop/Graham/CIT/git/PythonBootcamp/11 - Decorators/1 - Part 1.py", line 79, in <module>
#     print hello()
# NameError: name 'hello' is not defined

print greet()
# Hello Graham