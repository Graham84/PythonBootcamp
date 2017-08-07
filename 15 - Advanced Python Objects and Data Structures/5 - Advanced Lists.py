# Advanced Lists
# In this series of lectures we will be diving a little deeper into
# all the methods available in a list object. These aren't
# officially "advanced" features, just methods that you wouldn't
# typically encounter without some additional exploring. Its pretty
# likely that you've already encountered some of these yourself!
# Lets begin!

l = [1,2,3]

# append
# You will have definitely have use this method by now, which
# merely appends an element to the end of a list:
l.append(4)
print l
# [1, 2, 3, 4]

# count
# We discussed this during the methods lectures, but here it is again.
# count() takes in an element and returns the number of times it
# occurs in your list:
print l.count(10)
# 0
print l.count(2)
# 1

# extend
# Many times people find the difference between extend and append
# to be unclear. So note:
# append: Appends object at end
x = [1, 2, 3]
x.append([4, 5])
print x
# [1, 2, 3, [4, 5]]

# extend: extends list by appending elements from the iterable
x = [1, 2, 3]
x.extend([4, 5])
print x
# [1, 2, 3, 4, 5]
# Note how extend append each element in that iterable.
# That is the key difference.

# index
# index will return the index of whatever element is placed as an
# argument. Note: If the the element is not in the list an error
# is returned.
print l.index(2)
# 1
# print l.index(12)
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-11-3f090052d656> in <module>()
# ----> 1 l.index(12)
#
# ValueError: 12 is not in list
# insert
# insert takes in two arguments: insert(index,object) This method places the object at the index supplied. For example:

print l
# [1, 2, 3, 4]
# Place a letter at the index 2
l.insert(2,'inserted')
print l
# [1, 2, 'inserted', 3, 4]

# pop
# You most likely have already seen pop(), which allows us to "pop"
# off the last element of a list.
ele = l.pop()
print l
# [1, 2, 'inserted', 3]
print ele
# 4

# remove
# The remove() method removes the first occurrence of a value.
# For example:
print l
# [1, 2, 'inserted', 3]
l.remove('inserted')
print l
# [1, 2, 3]

l = [1,2,3,4,3]
l.remove(3)
print l
# [1, 2, 4, 3]

# reverse
# As you might have guessed, reverse() reverses a list.
# Note this occurs in place! Meaning it effects your list permanently.
l.reverse()
print l
# [3, 4, 2, 1]

# sort
# sort will sort your list in place:
print l
# [3, 4, 2, 1]
l.sort()
print l
# [1, 2, 3, 4]

# Great! You should now have an understanding of all the methods
# available for a list in Python!
