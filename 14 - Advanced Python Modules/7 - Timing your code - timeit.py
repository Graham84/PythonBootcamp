# Timing your code

# Sometimes its important to know how long your code is
# taking to run, or at least know if a particular line of
# code is slowing down your entire project. Python has a
# built-in timing module to do this.

# This module provides a simple way to time small bits of
# Python code. It has both a Command-Line Interface as well
# as a callable one. It avoids a number of common traps for
# measuring execution times.

# Lets learn about timeit!
import timeit

# Lets use time it to time various methods of creating the
# string '0-1-2-3-.....-99'

# We'll pass two arguments the actual line we want to test
# encapsulated as a string and the number of times we wish
# to run it. Here we'll choose 10,000 runs to get some high
# enough numbers to compare various methods.

# For loop
print timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# 0.349035711752

# List comprehension
print timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# 0.32651624237

# Map()
print timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# 0.210064955202

# Great! We see a significant time difference by using map()!
# This is good to know and we should keep this in mind.

# Now lets introduce iPython's magic function %timeit

# iPython's %timeit will perform the code in the same line a
# certain number of times (loops) and will give you the
# fastest performance time (best of 3).


# Lets repeat the above examinations using iPython magic!
# %timeit "-".join(str(n) for n in range(100))
# 10000 loops, best of 3: 23.8 µs per loop

# %timeit "-".join([str(n) for n in range(100)])
# 10000 loops, best of 3: 21.3 µs per loop

# %timeit "-".join(map(str, range(100)))
# 100000 loops, best of 3: 13.5 µs per loop

# Great! We arrie at the same conclusion. Its also important
# to note that iPython will limit the amount of real time it
# will spend on its timeit procedure. For instance if running
# 100000 loops took 10 minutes, iPython would automatically
# reduce the number of loops to something more reasonable like
# 100 or 1000.

# Great! You should now feel comfortable timing lines of your
# code, both in and out of iPython. Check out the documentation
# for more information:
# https://docs.python.org/2/library/timeit.html
