# OrderedDict
# An OrderedDict is a dictionary subclass that remembers the
# order in which its contents are added.

# For example a normal dictionary:

print 'Normal dictionary:'

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v


# Normal dictionary:
# a A
# c C
# b B
# e E
# d D


# An Ordered Dictionary:
import collections
print 'OrderedDict:'

d = collections.OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v


# OrderedDict:
# a A
# b B
# c C
# d D
# e E


# Equality with an Ordered Dictionary
# A regular dict looks at its contents when testing for equality.
# An OrderedDict also considers the order the items were added.
# A normal Dictionary:
print 'Dictionaries are equal? '

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

# Dictionaries are equal?
# True


# An Ordered Dictionary:
print 'Dictionaries are equal? '

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = collections.OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2
# Dictionaries are equal?
# False
