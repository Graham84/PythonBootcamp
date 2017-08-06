# Iterators and Generators Homework
# Problem 1
# Create a generator that generates the squares of numbers up
# to some number N.


def gensquares(N):
    for i in range(N):
        yield i ** 2

for x in gensquares(10):
    print x


# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81


# Problem 2
# Create a generator that yields "n" random numbers between a
# low and high number (that are inputs). Note: Use the random
# library. For example:

import random

random.randint(1, 10)
# 6


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1, 10, 12):
    print num

# 6
# 7
# 6
# 9
# 9
# 4
# 3
# 7
# 8
# 1
# 6
# 1


# Problem 3
# Use the iter() function to convert the string below

s = 'hello'
# code here

s = iter(s)

print next(s)


# Problem 4
# Explain a use case for a generator using a yield statement
# where you would not want to use a normal function with a
# return statement.
# Extra Credit!
# Can you explain what gencomp is in the code below?
# (Note: We never covered this in lecture! You will have to do
# some googling/Stack Overflowing!)

my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print item


# 4
# 5
# Hint google: generator comprehension is!
# Great Job!