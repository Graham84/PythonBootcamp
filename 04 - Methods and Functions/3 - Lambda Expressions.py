# Lambda Expressions

'''
One of Pythons most useful (and for beginners, confusing) tools is the lambda expression.L
ambda expressions allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions
without needing to properly define a function using def.
Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs.
There is key difference that makes lambda useful in specialized roles:
lambda's body is a single expression, not a block of statements.
The lambda's body is similar to what we would put in a def body's return statement.
simply type the result as an expression instead of explicitly returning it.
Because it is limited to an expression, a lambda is less general that a def.
We can only squeeze design, to limit program nesting.
lambda is designed for coding simple functions, and def handles the larger tasks.
Lets slowly break down a lambda expression by deconstructing a function:
'''


def square(num):
    result = num**2
    return result

print square(2)
# 4

# Continuing the breadown
def square(num):
    return num**2

print square(2)

# This is the form a function that a lambda expression intends to replicate. A lambda expression can then be written as:
print type(lambda num: num ** 2)


# Note how we get a function back. We can assign this function to a label:
square = lambda num: num**2
print square(2)

# Example 1
# Check if the number is even
even = lambda x: x % 2 == 0
print even(3)   # False
print even(4)   # True

# Example 2
# Grab first character of a string:
first = lambda s: s[0]
print first('hello')

# Example 3
# Reverse a string:
rev = lambda s: s[::-1]
print rev('hello')

# Example 4
# Just like a normal function, we can accept more than one function into a lambda expression:
adder = lambda x, y : x + y
print adder(2, 3)

'''
lambda expressions really shine when used in conjunction with map(),filter() and reduce().
Each of those functions has its own lecture, so feel free to explore them if you're very interested in lambda.
I highly recommend reading this blog post at Python Conquers the Universe for a great breakdown on lambda
expressions and some explanations of common confusions!
'''
# https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/
