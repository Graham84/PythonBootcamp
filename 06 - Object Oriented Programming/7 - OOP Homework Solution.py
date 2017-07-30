# Object Oriented Programming
# Homework Assignment

# Problem 1
# Fill in the Line class methods to accept coordinate as a pair
# of tuples and return the slope and distance of the line.

class Line(object):
    def __init__(self, coor1, coor2):
        print "A line has been created"
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        # ** 0.5 = square root
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return float((y2 - y1)) / (x2 - x1)

# EXAMPLE OUTPUT

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print li.distance()
# 9.433981132056603

print li.slope()
# 1.6


# Problem 2
# Fill in the class
class Cylinder(object):

    # Class object attribute
    pi = 3.14

    def __init__(self, height=1, radius=1):
        print "A cyclinder has been created"
        self.height = height
        self.radius = radius

    def volume(self):
        # v = Pi(R**2)H
        v = Cylinder.pi * (self.radius ** 2) * self.height
        return v
        # return self.height * (3.14) * (self.radius) ** 2

    def surface_area(self):
        # a = 2PiRH + 2Pi(R**2)
        a = (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * (self.radius ** 2))
        return a
        # top = (3.14) * (self.radius)** 2
        # return 2 * top + 2 * 3.14 * self.radius * self.height
# EXAMPLE OUTPUT
c = Cylinder(2, 3)

print c.volume()
# 56.52

print c.surface_area()
# 94.2
