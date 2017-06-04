# Chained Comparison Operators
'''
An interesting feature of Python is the ability to chain multiple comparisons to perform a more complex test. You can use these chained comparisons as a shorthand for larger Boolean Expressions.
In this lecture we will learn how to chain comparison operators and we will also introduce two other important statements in python: and and or.
'''

# Let's look at a few examples of using chains:
print 1 < 2 < 3
# True

# The above statsement check if 1 was less than 2 and if 2 was less than 3. We could have written this using an and statement in Python:
print 1 < 2 and 2 < 3
# True

# The and is used to make sure two checks have to be true in order for the total check to be true. Let's see another example:
print 1 < 3 > 2
# True
# The above checks if 3 is larger than both the other numbers, so you could use and to rewrite it as:
print 1 < 3 and 3 > 2
# True
# Its important to note that Python is checking both instances of the comparisons. We can also use or to write comparisons in Python. For example:
print 1 == 2 or 2 < 3
# True
# Note how it was true, this is because with the or operator, we only need one or the other two be true. Let's see one more example to drive this home:
print 1 == 1 or 100 == 1
# True
# Great! For an overview of this quick lesson: You should have a comfortable understanding of using and and or statements as well as reading chained comparison code.
# Go ahead and go to the quiz for this section to check your understanding!


# Chained Comparison Operators
'''
An interesting feature of Python is the ability to chain multiple comparisons to perform a more complex test. You can use these chained comparisons as a shorthand for larger Boolean Expressions.
In this lecture we will learn how to chain comparison operators and we will also introduce two other important statements in python: and and or.
'''

# Let's look at a few examples of using chains:
print 1 < 2 < 3
# True

# The above statsement check if 1 was less than 2 and if 2 was less than 3. We could have written this using an and statement in Python:
print 1 < 2 and 2 < 3
# True

# The and is used to make sure two checks have to be true in order for the total check to be true. Let's see another example:
print 1 < 3 > 2
# True
# The above checks if 3 is larger than both the other numbers, so you could use and to rewrite it as:
print 1 < 3 and 3 > 2
# True
# Its important to note that Python is checking both instances of the comparisons. We can also use or to write comparisons in Python. For example:
print 1 == 2 or 2 < 3
# True
# Note how it was true, this is because with the or operator, we only need one or the other two be true. Let's see one more example to drive this home:
print 1 == 1 or 100 == 1
# True
# Great! For an overview of this quick lesson: You should have a comfortable understanding of using and and or statements as well as reading chained comparison code.
# Go ahead and go to the quiz for this section to check your understanding!


