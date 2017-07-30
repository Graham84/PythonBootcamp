# Special Methods

# Finally lets go over special methods.
# Classes in Python can implement certain operations with
# special method names.
# These methods are not actually called directly but by
# Python specific language syntax.
# For example Lets create a Book class:

class Book(object):
    def __init__(self, title, author, pages):
        print "A book is created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, Author: %s, Pages: %s " %(self.title, self.author, self.pages)

    def __len__(self):
        return  self.pages

    def __del__(self):
        print "A book is destroyed"

book = Book("Python Rocks!", "Graham O Siochain", 169)

#Special Methods
print book
print len(book)
del book

# A book is created
# Title:Python Rocks! , author:Jose Portilla, pages:159
# 159
# A book is destroyed

# The __init__(), __str__(), __len__() and the __del__() methods.

# These special methods are defined by their use of underscores.
# They allow us to use Python specific functions on objects
# created through our class.

# Great! After this lecture you should have a basic understanding
# of how to create your own objects with class in Python.
# You will be utilizing this heavily in your next milestone
# project!

# For more great resources on this topic, check out:
# https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
# https://developer.mozilla.org/en-US/docs/Learn/Drafts/Python/Quickly_Learn_Object_Oriented_Programming
# http://www.tutorialspoint.com/python/python_classes_objects.htm
# https://docs.python.org/2/tutorial/classes.html
