# Comparison Operators

'''
In this lecture we will be learning about Comparison Operators in Python. These operators will allow us to compare variables and output a Boolean value (True or False).
If you have any sort of background in Math, these operators should be very straight forward.
First we'll present a table of the comparison operators and then work through some examples:
'''

# Table of Comparison Operators
# Operator	    Description	Example
# ==        	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
# !=        	If values of two operands are not equal, then condition becomes true.	(a != b) is true
# <>        	If values of two operands are not equal, then condition becomes true.	(a <> b) is true. This is similar to != operator.
# >         	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
# <         	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
# >=        	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
# <=	        If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.

#   Let's now work through quick examples of each of these.
#   Equal
print 2 == 2
# True
print 1 == 0
# False

# Not Equal
print 2 != 1
# True
print 2 != 2
# False
print 2 <> 1
# True
print 2 <> 2
# False

# Greater Than
print 2 > 1
# True
print 2 > 4
# False

# Less Than
print 2 < 4
# True
print 2 < 1
# False

# Greater Than or Equal to
print 2 >= 2
# True
print 2 >= 1
# True

# Less than or Equal to
print 2 <= 2
# True
print 2 <= 4
# True

# Great! Go over each comparison operator to make sure you understand what each one is saying.
# But hopefully this was straightforward for you
# Next we will cover chained comparison operators
