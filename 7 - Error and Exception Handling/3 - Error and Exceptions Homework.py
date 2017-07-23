# Errors and Exceptions Homework -
# Problem 1
# Handle the exception thrown by the code below by using
# try and except blocks.

for i in ['a', 'b', 'c']:
    try:
        print i ** 2
    except:
        print "An error occured"

# ---------------------------------------------------------------------------
# TypeError
# Traceback (most recent call last)
# <ipython-input-1-908335551eea> in <module>()
#       1 for i in ['a','b','c']:
# ----> 2     print i**2
#
# TypeError: unsupported operand type(s) for ** or pow():
# 'str' and 'int'


# Problem 2
# Handle the exception thrown by the code below by using try
# and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

try:
    z = x / y
except:
    print "An error occured"
finally:
    print "All Done"
# ---------------------------------------------------------------------------
# ZeroDivisionError
# Traceback (most recent call last)
# <ipython-input-2-3effb78be709> in <module>()
#       2 y = 0
#       3
# ----> 4 z = x/y
#
# ZeroDivisionError: integer division or modulo by zero


# Problem 3
# Write a function that asks for an integer and prints the
# square of it. Use a while loop with a try,except, else block
# to account for incorrect inputs.

def ask():
    while True:
        try:
            val = int(raw_input("Please enter an integer: "))
        except:
            print "Looks like you did not enter an int"
            continue
        else:
            print "Thank you"
            break
        finally:
            print "Finally executed"
    print val ** 2
ask()

# Input an integer: null
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, you number squared is:  4

# Great Job!