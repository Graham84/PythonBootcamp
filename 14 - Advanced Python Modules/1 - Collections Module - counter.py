# Collections Module
# The collections module is a built-in module that implements
# specialized container data types providing alternatives to
# Python's general purpose built-in containers.
# We've already gone over the basics: dict, list, set, and tuple.

# Now we'll learn about the alternatives that the collections
# module provides.

# Counter
# Counter is a dict subclass which helps count hash-able objects.
# Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.
# Lets see how it can be used:

from collections import Counter
# Counter() with lists
l = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]
print Counter(l)

# Counter with strings
x = 'aabsbsbsbhshhbbsbs'
print Counter(x)

# Counter with words in a sentence
s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
print Counter(words)


# Methods with Counter()
c = Counter(words)
print c.most_common(2)

# Common patterns when using the Counter() object
# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts
