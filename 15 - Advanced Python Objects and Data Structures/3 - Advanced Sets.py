# Advanced Sets
# In this lecture we will learn about the various methods for sets
# that you may not have seen yet. We'll go over the basic ones you
# already know and then dive a little deeper.

s = set()
# add
# add elements to a set. Remember a set won't take duplicate elements
# and only present them once (thats why its called a set!)
s.add(1)
s.add(2)
print s
# {1, 2}

# clear
# removes all elements from the set
s.clear()
print s
# set()

# copy
# returns a copy of the set. Note it is a copy, so changes to the
# original don't effect the copy.
s = {1, 2, 3}
sc = s.copy()
print sc
# {1, 2, 3}
print s
# {1, 2, 3}

s.add(4)
print s
# {1, 2, 3, 4}
print sc
# {1, 2, 3}

# difference
# difference returns the difference of two or more sets.
# The syntax is:
# set1.difference(set2)
# For example:
print s.difference(sc)
# {4}

# difference_update
# difference_update syntax is:
# set1.difference_update(set2)
# the method returns set1 after removing elements found in set2
s1 = {1, 2, 3}
s2 = {1, 4, 5}
print s1.difference_update(s2)
print s1
# {2, 3}

# discard
# Removes an element from a set if it is a member.If the element is
# not a member, do nothing.
print s
# {1, 2, 3}
s.discard(2)
print s
# {1, 3}

# intersection and intersection_update
# Returns the intersection of two or more sets as a new set.
# (i.e. elements that are common to all of the sets.)
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print s1.intersection(s2)
# {1, 2}
print s1
# {1, 2, 3}
# intersection_update will update a set with the intersection of
# itself and another.
print s1.intersection_update(s2)
print s1
# {1, 2}

# isdisjoint
# This method will return True if two sets have a null intersection.
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
print s1.isdisjoint(s2)
# False
print s1.isdisjoint(s3)
# True

# issubset
# This method reports whether another set contains this set.
print s1
# {1, 2}
print s2
# {1, 2, 4}
print s1.issubset(s2)
# True

# issuperset
# This method will report whether this set contains another set.
print s2.issuperset(s1)
# True

# symmetric_difference and symmetric_update
# Return the symmetric difference of two sets as a new set.
# (i.e. all elements that are in exactly one of the sets.)
print s1
# {1, 2}
print s2
# {1, 2, 4}
print s1.symmetric_difference(s2)
# {4}

# union
# Returns the union of two sets
# (i.e. all elements that are in either set.)
print s1.union(s2)
# {1, 2, 4}

# update
# Update a set with the union of itself and others.
s1.update(s2)
print s1
# {1, 2, 4}

# Great! You should now have a complete awareness of all the methods
# available to you for a set object type. This data structure is
# extremely useful and is underutilized by beginners, so try to
# keep it in mind!

# Good Job!
