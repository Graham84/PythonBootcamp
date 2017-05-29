# Tuples
'''
In Python tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed.
You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.
In this section, we will get a brief overview of the following:
1.) Constructing Tuples
2.) Basic Tuple Methods
3.) Immutability
4.) When to Use Tuples.
'''

# You'll have an intuition of how to use tuples based on what you've learned about lists.
# We can treat them very similarly with the major distinction being that tuples are immutable.
# Constructing Tuples
# The construction of a tuples use () with elements separated by commas. For example:

# Can create a tuple with mixed types
t = (1,2,3)
# Check len just like a list
print len(t)
# 3

# Can also mix object types
t = ('one',2)
# Show
print t
# ('one', 2)

# Use indexing just like we did in lists
print t[0]
# 'one'

# Slicing just like a list
print t[-1]
# 2

# Basic Tuple Methods
# Tuples have built-in methods, but not as many as lists do. Lets look at two of them:

# Use .index to enter a value and return the index
print t.index('one')
# 0

# Use .count to count the number of times a value appears
print t.count('one')
# 1

# Immutability
# It can't be stressed enough that tuples are immutable. To drive that point home:
# t[0]= 'change'
'''
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-93def5f9b4bd> in <module>()
----> 1 t[0]= 'change'

TypeError: 'tuple' object does not support item assignment
Because of this immutability, tuples can't grow. Once a tuple is made we can not add to it.
'''

# t.append('nope')
'''
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-15-799b3447c4d9> in <module>()
----> 1 t.append('nope')

AttributeError: 'tuple' object has no attribute 'append'
'''

# When to use Tuples
# You may be wondering, "Why bother using tuples when they have fewer available methods?"
# To be honest, tuples are not used as often as lists in programming, but are used when immutability is necessary.
# If in your program you are passing around an object and need to make sure it does not get changed, then tuple become your solution.
# It provides a convenient source of data integrity.
# You should now be able to create and use tuples in your programming as well as have an understanding of their immutability.
# Up next Files!