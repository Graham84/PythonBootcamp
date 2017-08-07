# StringIO
# The StringIO module implements an in-memory file like object.
# This object can then be used as input or output to most functions
# that would expect a standard file object.

# The best way to show this is by example:

import StringIO
# Arbitrary String
message = 'This is just a normal string.'


# Use StringIO method to set as file object
f = StringIO.StringIO(message)

# Now we have an object f that we will be able to treat just
# like a file. For example:

f.read()
# ''

# We can also write to it:
f.write(' Second line written to file like object')

# Reset cursor just like you would a file
f.seek(0)

# Read again
f.read()

# 'This is just a normal string. Second line written to file
# like object'

# Great! Now you've seen how we can use StringIO to turn normal
# strings into in-memory file objects in our code. This kind of
# action has various use cases, especially in web scraping
# cases where you want to read some string you scraped as a file.

# For more info on StringIO check out the documentation:
# https://docs.python.org/2/library/stringio.html
