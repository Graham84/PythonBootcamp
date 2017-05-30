# Objects and Data Structures Assessment Test

'''
Test your knowledge.
Answer the following questions
Write a brief description of all the following Object Types and Data Structures we've learned about:
For the full answers, review the Jupyter notebook introductions of each topic!
Numbers
Strings
Lists
Tuples
Dictionaries
Numbers
'''

# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

# Your answer is probably different
a = (20000 - (10 ** 2) / 12 * 34) - 19627.75
print a
# 100.25

# Explain what the cell below will produce and why. Can you change it so the answer is correct?
print 2/3
# 0

# Answer: Because Python 2 performs classic division for integers. Use floats to perform true division. For example: 2.0/3
#  Answer these 3 questions without typing code. Then type code to check your answer.
# What is the value of the expression 4 * (6 + 5)
# What is the value of the expression 4 * 6 + 5
# What is the value of the expression 4 + 6 * 5

print 4 * (6 + 5)
# 44
print 4 * 6 + 5
# 29
print 4 + 6 * 5
# 34

# What is the type of the result of the expression 3 + 1.5 + 4?
# Answer: Floating Point Number

# What would you use to find a number's square root, as well as its square?
print 100 ** 0.5
# 10.0
print 10 ** 2
# 1100

# Strings
# Given the string 'hello' give an index command that returns 'e'. Use the code below:
s = 'hello'
# Print out 'e' using indexing
print s[1]
# 'e'

# Reverse the string 'hello' using indexing:
s ='hello'

# Reverse the string using indexing
print s[::-1]
'olleh'

# Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'

# Print out the
print s[-1]
# 'o'

print s[4]
# 'o'

# Lists
# Build this list [0,0,0] two separate ways.

#Method 1
a = [0]*3
print a
# [0, 0, 0]

#Method 2
l = [0,0,0]
print l
# [0, 0, 0]

# Reassign 'hello' in this nested list to say 'goodbye' item in this list:
l = [1,2,[3,4,'hello']]
l[2][2] = 'goodbye'
print l
# [1, 2, [3, 4, 'goodbye']]

# Sort the list below:
l = [3,4,5,5,6]

#Method 1
print sorted(l)
# [3, 4, 5, 5, 6]

#Method 2
l.sort()
print l
# [3, 4, 5, 5, 6]

# Dictionaries
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}

# Grab 'hello'

print d['simple_key']
# 'hello'
d = {'k1':{'k2':'hello'}}

# Grab 'hello'
print d['k1']['k2']
# 'hello'

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# This was harder than I expected...
print d['k1'][0]['nest_key'][1][0]
# 'hello'

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

# Phew
print d['k1'][2]['k2'][1]['tough'][2][0]
# 'hello'

# Can you sort a dictionary? Why or why not?
# Answer: No! Because normal dictionaries are mappings not a sequence.

# Tuples
# What is the major difference between tuples and lists?
# Tuples are immutable!
# How do you create a tuple?
t = (1,2,3)
print t


# Sets
# What is unique about a set?
# Answer: They don't allow for duplicate items!
# Use a set to find the unique values of the list below:

l = [1,2,2,33,4,4,11,22,3,3,2]

print set(l)
# {1, 2, 3, 4, 11, 22, 33}

# Booleans
# For the following quiz questions, we will get a preview of comparison operators:
#  Operator	Description	Example
# ==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
# !=	If values of two operands are not equal, then condition becomes true.
# <>	If values of two operands are not equal, then condition becomes true.	(a <> b) is true. This is similar to != operator.
# >	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
# <	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
# >=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
# <=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.

# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)
# Answer before running cell
print 2 > 3
# False

# Answer before running cell
print 3 <= 2
# False

# Answer before running cell
print 3 == 2.0
# False

# Answer before running cell
print 3.0 == 3
# True

# Answer before running cell
print 4**0.5 != 2
# False

# Final Question: What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

#True or False?
print l_one[2][0] >= l_two[2]['k1']
# False