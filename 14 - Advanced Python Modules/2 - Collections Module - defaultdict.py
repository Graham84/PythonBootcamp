# defaultdict
# defaultdict is a dictionary like object which provides all
# methods provided by dictionary but takes first argument
# (default_factory) as default data type for the dictionary.
# Using defaultdict is faster than doing the same using
# dict.set_default method.

# A defaultdict will never raise a KeyError.
# Any key that does not exist gets the value returned
# by the default factory.

from collections import defaultdict
d = {}


# d['one']

# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-22-07706fc5dc20> in <module>()
# ----> 1 d['one']
#
# KeyError: 'one'


d = defaultdict(object)
print d['one']
# <object at 0x1002c3a50>


for item in d:
    print item

# one
# Can also initialize with default values:

d = defaultdict(lambda: 0)
print d['one']
# 0
