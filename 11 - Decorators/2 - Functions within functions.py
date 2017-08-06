# Functions within functions
# Great! So we've seen how we can treat functions as objects,
# now lets see how we can define functions inside of other functions:


def hello(name='Jose'):
    print 'The hello() function has been executed'

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    print greet()
    print welcome()
    print "Now we are back inside the hello() function"

print hello()
# The hello() function has been executed
# 	 This is inside the greet() function
# 	 This is inside the welcome() function
# Now we are back inside the hello() function

# print welcome()

# Traceback (most recent call last):
#   File "C:/Users/Graham/Desktop/Graham/CIT/git/PythonBootcamp/11 - Decorators/2 - Functions within functions.py", line 25, in <module>
#     print welcome()
# NameError: name 'welcome' is not defined

# Note how due to scope, the welcome() function is not defined
# outside of the hello() function.
# Now lets learn about returning functions from within functions:

# Returning Functions

def hello(name='Jose'):
    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Jose':
        return greet
    else:
        return welcome

x = hello()
# Now lets see what function is returned if we set x = hello(),
# note how the closed parenthesis means that name ahs been
# defined as Jose.

print x
# <function greet at 0x02512B30>

# Great! Now we can see how x is pointing to the greet function
# inside of the hello function.

print x()
# Lets take a quick look at the code again.

# In the if/else clause we are returning greet and welcome,
# not greet() and welcome().

# This is because when you put a pair of parentheses after it,
# the function gets executed; whereas if you don't put parenthesis
# after it, then it can be passed around and can be assigned to
#  other variables without executing it.

# When we write x = hello(), hello() gets executed and because
# the name is Jose by default, the function greet is returned.
# If we change the statement to x = hello(name = "Sam") then the
# welcome function will be returned.
# We can also do print hello()() which outputs
# now you are in the greet() function.

