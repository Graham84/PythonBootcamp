# Functions as Arguments

# Now lets see how we can pass functions as arguments into
# other functions:


def hello():
    return 'Hi Jose!'


def other(func):
    print 'Other code would go here'
    print func()

print other(hello)

# Other code would go here
# Hi Jose!

# Great! Note how we can pass the functions as objects and then
# use them within other functions. Now we can get started with
# writing our first decorator:

# Creating a Decorator
# In the previous example we actually manually created a Decorator.
# Here we will modify it to make its use case clear:


def new_decorator(func):
    def wrap_func():
        print "Code would be here, before executing the func"
        func()
        print "Code here will execute after the func()"
    return wrap_func


def func_needs_decorator():
    print "This function is in need of a Decorator"

print func_needs_decorator()
# "This function is in need of a Decorator"

# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

print func_needs_decorator()

# Code would be here, before executing the func
# This function is in need of a Decorator
# Code here will execute after the func()

# So what just happened here? A decorator simple wrapped the
# function and modified its behavior. Now lets understand how
# we can rewrite this code using the @ symbol, which is
# uses for Decorators:

@new_decorator
def func_needs_decorator():
    print "This function is in need of a Decorator"

print func_needs_decorator
print func_needs_decorator()


# Code would be here, before executing the func
# This function is in need of a Decorator
# Code here will execute after the func()

# Great! You've now built a Decorator manually and then saw how
# we can use the @ symbol in Python to automate this and clean
# our code. You'll run into Decorators a lot if you begin using
# Python for Web Development, such as Flask or Django!
