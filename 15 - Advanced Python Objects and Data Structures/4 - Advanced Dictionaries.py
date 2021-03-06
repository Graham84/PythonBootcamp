# Advanced Dictionaries
# Unlike some of the other Data Structures we've worked with,
# most of the really useful methods available to us in Dictionaries
# have already been explored throughout this course. Here we will
# touch on just a few more for good measure:

d = {'k1': 1, 'k2': 2}

# Dictionary Comprehensions
# Just like List Comprehensions, Dictionary Data Types also support
# their own version of comprehension for quick creation. It is not
# as commonly used as List Comprehensions, but the syntax is:
{x:x**2 for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# One of the reasons it is not as common is the difficulty in
# structuring the key names that are not based off the values.

# Iteration over keys,values, and items
# Dictionaries can be iterated over using the iter methods available
# in a dictionary. For example:
for k in d.iterkeys():
    print k
# k2
# k1

for v in d.itervalues():
    print v
# 2
# 1

for item in d.iteritems():
    print item
# ('k2', 2)
# ('k1', 1)

# view items,keys and values
# You can use the view methods to view items keys and values.
# For example:
print d.viewitems()
# dict_items([('k2', 2), ('k1', 1)])

print d.viewkeys()
# dict_keys(['k2', 'k1'])

print d.viewvalues()
# dict_values([2, 1])

# Great! You should now feel very comfortable using the variety of
# methods available to you in Dictionaries!
