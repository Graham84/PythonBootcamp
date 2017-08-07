# Advanced Numbers
# In this lecture we will learn about a few more representations
# of numbers in Python.

# Hexadecimal
# Using the function hex() you can convert numbers into a hexadecimal
# format:

print hex(246)
# 0xf6
print hex(512)
# 0x200


# Binary
# Using the function bin() you can convert numbers into their
# binary format.

print bin(1234)
# 0b10011010010
print bin(128)
# 0b10000000
print bin(512)
# 0b10000000000


# pow()
# With two arguments, equivalent to x^y. With three arguments,
# equivalent to (x^y) % z, but may be more efficient (e.g. for longs).

print pow(2,4)
# 16


# abs
# Absolute Value
print abs(-3)
# 3
print abs(3)
# 3


# round
# Round a number to a given precision in decimal digits
# (default 0 digits). This always returns a floating point number.

print round(3)
# 3.0
print round(3.1415926535, 2)
# 3.14

# Python has a built-in math library that is also useful to play
# around with in case you are ever in need of some mathematical
# operations. Explore the documentation here!
