# Advanced Strings
# String objects have a variety of methods we can use to save time
# and add functionality. Lets explore some of them in this lecture:

s = 'hello world'

# Changing case
# We can use methods to capitalize the first word of a string,
# change cases to upper and lower case strings.

# Capitalize first word in string
print s.capitalize()
# 'Hello world'
print s.upper()
# 'HELLO WORLD'
print s.lower()
# 'hello world'


# Location and Counting
print s.count('o')
# 2
print s.find('o')
# 4


# Formatting
# The center() method allows you to place your string 'centered'
# between a provided string with a certain length.
# Personally, I've never actually used this in code as it seems
# pretty esoteric...
print s.center(20, 'z')
# 'zzzzhello worldzzzzz'

# expandtabs() will expand tab notations \t into spaces:
print 'hello\thi'.expandtabs()
# 'hello   hi'


# is check methods
# These various methods below check it the string is some case. Lets explore them:

s = 'hello'
# isalnum() will return True if all characters in S are alphanumeric
print s.isalnum()
# True

# isalpha() wil return True if all characters in S are alphabetic
print s.isalpha()
# True

# islower() will return True if all cased characters in S are
# lowercase and there is at least one cased character in S,
# False otherwise.
print s.islower()
# True

# isspace() will return True if all characters in S are whitespace.
print s.isspace()
# False

# istitle() will return True if S is a title cased string and there
# is at least one character in S, i.e. uppercase characters may only
# follow uncased characters and lowercase characters only cased ones.
# Return False otherwise.
print s.istitle()
# False

# isupper() will return True if all cased characters in S are
# uppercase and there is at least one cased character in S,
# False otherwise.
print s.isupper()
# False

# Another method is endswith() which is essentially the same
# as a boolean check on s[-1]
print s.endswith('o')
# True


#  Built-in Reg. Expressions
# Strings have some built-in methods that can resemble regular
# expression operations. We can use split() to split the string
# at a certain element and return a list of the result. We can use
# partition to return a tuple that includes the separator
# (the first occurrence) and the first half and the end half.
print s.split('e')
# ['h', 'llo']
print s.partition('e')
# ('h', 'e', 'llo')
print s
# 'hello'

# Great! You should now feel comfortable using the variety of methods
# that are built-in string objects!
