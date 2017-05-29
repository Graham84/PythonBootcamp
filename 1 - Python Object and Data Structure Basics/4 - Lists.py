# Lists

'''
Earlier when discussing strings we introduced the concept of a sequence in Python. Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed!
In this section we will learn about:
1.) Creating lists
2.) Indexing and Slicing Lists
3.) Basic List Methods
4.) Nesting Lists
5.) Introduction to List Comprehensions
'''

# Lists are constructed with brackets [] and commas separating every element in the list.
# Let's go ahead and see how we can construct lists!

# Assign a list to an variable named my_list
my_list = [1, 2, 3]
print my_list

# We just created a list of integers, but lists can actually hold different object types. For example:
my_list = ['A string', 23, 100.232, 'o']
print my_list

# Just like strings, the len() function will tell you how many items are in the sequence of the list.
print len(my_list)


# Indexing and Slicing
# Indexing and slicing works just like in strings. Let's make a new list to remind ourselves of how this works:
my_list = ['one', 'two', 'three', 4, 5]
print my_list

# Grab element at index 0
print my_list[0]
# one

# Grab index 1 and everything past it
print my_list[1:]
# ['two', 'three', 4, 5]

# Grab everything UP TO index 3
print my_list[:3]
# ['one', 'two', 'three']

# We can also use + to concatenate lists, just like we did for strings.

print my_list + ['new item']
# ['one', 'two', 'three', 4, 5, 'new item']

# Note: This doesn't actually change the original list!
print my_list
# ['one', 'two', 'three', 4, 5]

# You would have to reassign the list to make the change permanent.
# Reassign
my_list = my_list + ['add new item permanently']

print my_list
# ['one', 'two', 'three', 4, 5, 'add new item permanently']
# We can also use the * for a duplication method similar to strings:

# Make the list double
print my_list * 2

'''
['one',
 'two',
 'three',
 4,
 5,
 'add new item permanently',
 'one',
 'two',
 'three',
 4,
 5,
 'add new item permanently']
'''

# Again doubling not permanent
print my_list
# ['one', 'two', 'three', 4, 5, 'add new item permanently']

# Basic List Methods
# If you are familiar with another programming language, you might start to draw parallels between arrays in another language and lists in Python.
# Lists in Python however, tend to be more flexible than arrays in other languages for a two good reasons: they have no fixed size (meaning we don't have
# to specify how big a list will be), and they have no fixed type constraint (like we've seen above).
# Let's go ahead and explore some more special methods for lists:

# Create a new list
l = [1, 2, 3]
# Use the append method to permanently add an item to the end of a list:

# Append
l.append('append me!')

# Show
print l
# [1, 2, 3, 'append me!']

# Use pop to "pop off" an item from the list. By default pop takes off the last index, but you can also specify which index to pop off. Let's see an example:
# Pop off the 0 indexed item
l.pop(0)

print 1
# [2, 3, 'append me!']

# Assign the popped element, remember default popped index is -1
popped_item = l.pop()

print popped_item
# 'append me!'

# Show remaining list
print l
# [2, 3]

# It should also be noted that lists indexing will return an error if there is no element at that index. For example:
# print l[100]
'''---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-50-3e7ce3111e95> in <module>()
----> 1 l[100]

IndexError: list index out of range'''

# We can use the sort method and the reverse methods to also effect your lists:
new_list = ['a', 'e', 'x', 'b', 'c']

#Show
print new_list

# ['a', 'e', 'x', 'b', 'c']
# Use reverse to reverse order (this is permanent!)

new_list.reverse()
print new_list
# ['c', 'b', 'x', 'e', 'a']

# Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
new_list.sort()
print new_list
# ['a', 'b', 'c', 'e', 'x']

# Nesting Lists
# A great feature of of Python data structures is that they support nesting. This means we can have data structures within data structures. For example: A list inside a list.
# Let's see how this works!

# Let's make three lists
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

# Make a list of lists to form a matrix
matrix = [lst_1, lst_2, lst_3]

# Show
print matrix
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Now we can again use indexing to grab elements, but now there are two levels for the index. The items in the matrix object, and then the items inside that list!
# Grab first item in matrix object
print matrix[0]
# [1, 2, 3]

# Grab first item of the first item in the matrix object
print matrix[0][0]
# 1

# List Comprehensions
# Python has an advanced feature called list comprehensions. They allow for quick construction of lists. To fully understand list comprehensions we need to understand for loops.
# So don't worry if you don't completely understand this section, and feel free to just skip it since we will return to this topic later.
# But in case you want to know now, here are a few examples!

# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]

print first_col
# 1, 4, 7]

# We used list comprehension here to grab the first element of every row in the matrix object. We will cover this in much more detail later on!
# For more advanced methods and features of lists in Python, check out the advanced list section later on in this course!
