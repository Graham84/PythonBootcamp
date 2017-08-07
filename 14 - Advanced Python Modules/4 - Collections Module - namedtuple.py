# namedtuple
# The standard tuple uses numerical indexes to
# access its members, for example:

t = (12, 13, 14)
print t[0]

# 12

# For simple use cases, this is usually enough.
# On the other hand, remembering which index should be
# used for each value can lead to errors, especially if
# the tuple has a lot of fields and is constructed far from
# where it is used. A namedtuple assigns names, as well as
# the numerical index, to each member.

# Each kind of namedtuple is represented by its own class,
# created by using the namedtuple() factory function.
# The arguments are the name of the new class and a string
# containing the names of the elements.

# You can basically think of namedtuples as a very quick way
# of creating a new object/class type with some attribute fields.
#  For example:

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='Lab', name='Sammy')

frank = Dog(age=2, breed='Shepard', name="Frankie")

print sam
# Dog(age=2, breed='Lab', name='Sammy')
print sam.age
# 2
print sam.breed
# Lab
print sam[0]
# 2

