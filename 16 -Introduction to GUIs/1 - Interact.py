# Using Interact
# In this lecture we will begin to learn about creating
# dashboard-type GUI with iPython widgets!

# The interact function (ipywidgets.interact) automatically
# creates user interface (UI) controls for exploring code
# and data interactively. It is the easiest way to get started
# using IPython's widgets.

# Start with some imports!
from __future__ import print_function
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
# Please Note! The widgets in this notebook won't show up on
# NbViewer or GitHub renderings. To view the widgets and
# interact with them, you will need to download this notebook
# and run it with a Jupyter Notebook server.

# Basic interact
# At the most basic level, interact auto-generates UI controls
# for function arguments, and then calls the function with those
# arguments when you manipulate the controls interactively.
# To use interact, you need to define a function that you want
# to explore. Here is a function that prints its only argument x.

# # Very basic function


def f(x):
    return x

# When you pass this function as the first argument to
# interact along with an integer keyword argument (x=10),
# a slider is generated and bound to the function parameter.
# Note that the semicolon here just prevents an out cell from
# showing up.

# # Generate a slider to interact with
interact(f, x=10,);
# -8
# When you move the slider, the function is called, which prints the current value of x.
# If you pass True or False, interact will generate a check-box:
# # Booleans generate check-boxes
interact(f, x=True);
# False

# If you pass a string, interact will generate a text area.
# Strings generate text areas
interact(f, x='Hi there!');
u'string'
# interact can also be used as a decorator. This allows you to
# define a function and interact with it in a single shot.
# As this example shows, interact also works with functions
# that have multiple arguments.
# Using a decorator!
@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)
# (True, 1.1)

# Fixing arguments using fixed
# There are times when you may want to explore a function using
# interact, but fix one or more of its arguments to specific
# values. This can be accomplished by wrapping values with the
# fixed function.
# Again, a simple function
def h(p, q):
    return (p, q)

# When we call interact, we pass fixed(20) for q to hold it
# fixed at a value of 20.
interact(h, p=5, q=fixed(20));
(13, 20)

# Notice that a slider is only produced for p as the value of q
# is fixed.

# Widget abbreviations
# When you pass an integer-valued keyword argument of 10 (x=10)
# to interact, it generates an integer-valued slider control
# with a range of $[-10,+3\times10]$. In this case, 10 is an
# abbreviation for an actual slider widget:
# IntSlider(min=-10,max=30,step=1,value=10)
# In fact, we can get the same result if we pass this IntSlider
# as the keyword argument for x:

# Can call the IntSlider to get more specific
interact(f, x=widgets.IntSlider(min=-10, max=30, step=1, value=10));
# 10
# This examples clarifies how interact process its keyword
# arguments:
# If the keyword argument is a Widget instance with a value
# attribute, that widget is used. Any widget with a value
# attribute can be used, even custom ones.
# Otherwise, the value is treated as a widget abbreviation that
# is converted to a widget before it is used.
# The following table gives an overview of different widget
# abbreviations:
# Keyword argument	Widget
# `True` or `False`	Checkbox
# `'Hi there'`	Text
# `value` or `(min,max)` or `(min,max,step)` if integers are passed	IntSlider
# `value` or `(min,max)` or `(min,max,step)` if floats are passed	FloatSlider
# `('orange','apple')` or `{'one':1,'two':2}`	Dropdown
# You have seen how the check-box and text-area widgets work
# above. Here, more details about the different abbreviations
# for sliders and drop-downs are given.
# If a 2-tuple of integers is passed (min,max), an integer-valued
# slider is produced with those minimum and maximum values
# (inclusively). In this case, the default step size of 1 is used.

# Min,Max slider with Tuples
interact(f, x=(0, 4));
# 2
# If a 3-tuple of integers is passed (min,max,step), the step size can also be set.
# (min, max, step)
interact(f, x=(0, 8, 2));
# 4
# A float-valued slider is produced if the elements of the
# tuples are floats. Here the minimum is 0.0, the maximum
# is 10.0 and step size is 0.1 (the default).
interact(f, x=(0.0, 10.0));
# 5.0
# The step size can be changed by passing a third element in
# the tuple.
interact(f, x=(0.0,10.0,0.01));
# 4.99
# For both integer and float-valued sliders, you can pick the
# initial value of the widget by passing a default keyword
# argument to the underlying Python function. Here we set the
# initial value of a float slider to 5.5.
@interact(x=(0.0,20.0,0.5))
def h(x=5.5):
    return x
# 5.5
# Dropdown menus are constructed by passing a tuple of strings.
# In this case, the strings are both used as the names in the
# drop-down menu UI and passed to the underlying Python function.
interact(f, x=('apples','oranges'));
u'apples'
# If you want a drop-down menu that passes non-string values to
# the Python function, you can pass a dictionary. The keys in
# the dictionary are used for the names in the drop-down menu
# UI and the values are the arguments that are passed to
# the underlying Python function.
interact(f, x={'one': 10, 'two': 20});
# 20
# Using function annotations with interact
# If you are using Python 3, you can also specify widget
# abbreviations using function annotations.
# PYTHON 3
# Define a function with a checkbox widget abbreviation for the
# argument x.
# def f(x:True): # python 3 only
#     return x
# Then, because the widget abbreviation has already been
# defined, you can call interact with a single argument.
# interact(f);

# PYTHON 2
# If you are running Python 2, function annotations can be
# defined using the @annotate function.
from IPython.utils.py3compat import annotate
@annotate(x=True)
def f(x):
    return x
interact(f);
# False

# interactive
# In addition to interact, IPython provides another function,
# interactive, that is useful when you want to reuse the
# widgets that are produced or access the data that is bound
# to the UI controls.

# Here is a function that returns the sum of its two arguments.
def f(a, b):
    return a+b
# Unlike interact, interactive returns a Widget instance
# rather than immediately displaying the widget.
w = interactive(f, a=10, b=20)
# The widget is a Box, which is a container for other widgets.
type(w)

ipywidgets.widgets.widget_box.Box
# The children of the Box are two integer-valued sliders
# produced by the widget abbreviations above.
w.children
# (<ipywidgets.widgets.widget_int.IntSlider at 0x104cdf210>,
#  <ipywidgets.widgets.widget_int.IntSlider at 0x104cd18d0>)

# To actually display the widgets, you can use IPython's
# display function.
from IPython.display import display
display(w)
# 30

# At this point, the UI controls work just like they would if
# interact had been used. You can manipulate them
# interactively and the function will be called.
# However, the widget instance returned by interactive
# also give you access to the current keyword arguments
# and return value of the underlying Python function.
# Here are the current keyword arguments. If you rerun this
# cell after manipulating the sliders, the values will have
# changed.
w.kwargs
# {'a': 10, 'b': 20}

# Here is the current return value of the function.
w.result
# 30

# Conclusion
# You should now have a basic understanding of how to use
# Interact in Jupyter Notebooks!
