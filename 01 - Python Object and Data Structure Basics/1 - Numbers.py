'''
Numbers and more in Python!
In this lecture, we will learn about numbers in Python and how to use them.
We'll learn about the following topics:
1.) Types of Numbers in Python
2.) Basic Arithmetic
3.) Differences between Python 2 vs 3 in division
4.) Object Assignment in Python
Types of numbers
Python has various "types" of numbers (numeric literals). We'll mainly focus on integers and floating point numbers.
Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.
Throughout this course we will be mainly working with integers or simple float number types.
Here is a table of the two main types we will spend most of our time working with some examples:
<table border = "1">
Examples Number "Type"
1,2,-5,1000 Integers
1.2,-0.5,2e2,3E2 Floating-point numbers
</table>
Now let's start with some basic arithmetic.
'''

# Basic Arithmetic

# Addition
print 2 + 1

# Subtraction
print 2 - 1

# Multiplication
print 2 * 2

# Division
print 3 / 2

# Whoa! What just happened? Last time I checked, 3 divided by 2 is equal 1.5 not 1!
# Specifying one of the numbers as a float
print 3.0 / 2

# Works for either number
print 3 / 2.0

# We can use this float() function to cast integers as floats:
print float(3) / 2

# from __future__ import division
print 3 / 2

# Powers
print 2 ** 3

# Can also do roots
print 4 ** 0.5

# Order of Operations followed in Python
print 2 + 10 * 10 + 3

# Can use parenthesis to sppecify orders
print (2 + 10) * (10 + 3)


# Variable Assignments

# Let's create an object called "a" and assign it the number 5
a = 5
print a

# Adding the objects
print a + a
print a

# Reassignment
a = 10
print a

# Use A to redefine A
a = a + a
print a

'''
The names you use when creating these labels need to follow a few rules:
1. Names can not start with a number.
2. There can be no spaces in the name, use _ instead.
3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
3. It's considered best practice (PEP8) that the names are lowercase.
'''

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate

print my_taxes
