# Methods

# Methods are functions defined inside the body of a class.
# They are used to perform operations with the attributes
# of our objects.
# Methods are essential in encapsulation concept of the
# OOP paradigm. This is essential in dividing responsibilities
# in programming, especially in large applications.

# You can basically think of methods as functions acting on
# an Object that take the Object itself into account through
# its self argument.

# Lets go through an example of creating a Circle class:

class Circle(object):
    pi = 3.14

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius

    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius

    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius


c = Circle()

c.setRadius(2)
print 'Radius is: ', c.getRadius()
print 'Area is: ', c.area()

# Radius is: 2
# Area is: 12.56

# Great! Notice how we used self. notation to reference
# attributes of the class within the method calls.
# Review how the code above works and try creating
# your own method
