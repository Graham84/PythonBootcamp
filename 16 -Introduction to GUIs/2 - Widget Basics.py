# Widget Basics
# In this lecture we will continue to build off our understanding of interact and interactive to begin using full widgets!
# What are widgets?
# Widgets are eventful python objects that have a representation in the browser, often as a control like a slider, text-box, etc.
# What can they be used for?
# You can use widgets to build interactive GUIs for your notebooks.
# You can also use widgets to synchronize stateful and stateless information between Python and JavaScript.
# Using widgets
# To use the widget framework, you need to import ipywidgets.
# In [1]:
# from ipywidgets import *
# repr
# Widgets have their own display repr which allows them to be displayed using IPython's display framework. Constructing and returning an IntSlider automatically displays the widget (as seen below). Widgets are displayed inside the widget area, which sits between the code cell and output. You can hide all of the widgets in the widget area by clicking the grey x in the margin.
# In [2]:
# IntSlider()
# display()
# You can also explicitly display the widget using display(...).
# In [3]:
# from IPython.display import display
# w = IntSlider()
# display(w)
# Multiple display() calls
# If you display the same widget twice, the displayed instances in the front-end will remain in sync with each other. Try dragging the slider below and watch the slider above.
# In [5]:
# display(w)
# Closing widgets
# You can close a widget by calling its close() method.
# In [6]:
# display(w)
# In [7]:
# w.close()
# Widget properties
# All of the IPython widgets share a similar naming scheme. To read the value of a widget, you can query its value property.
# In [8]:
# w = IntSlider()
# display(w)
# In [9]:
# w.value
# Out[9]:
# 0
# Similarly, to set a widget's value, you can set its value property.
# In [10]:
# w.value = 100
# Keys
# In addition to value, most widgets share keys, description, disabled, and visible. To see the entire list of synchronized, stateful properties of any specific widget, you can query the keys property.
# In [11]:
# w.keys
# Out[11]:
# ['_view_name',
#  'orientation',
#  'color',
#  '_view_module',
#  'height',
#  'disabled',
#  'visible',
#  'border_radius',
#  'border_width',
#  '_model_module',
#  'font_style',
#  'min',
#  '_range',
#  'background_color',
#  'slider_color',
#  'width',
#  'version',
#  'font_family',
#  '_dom_classes',
#  'description',
#  '_model_name',
#  'max',
#  'border_color',
#  'readout',
#  'padding',
#  'font_weight',
#  'step',
#  'border_style',
#  'font_size',
#  'msg_throttle',
#  '_css',
#  'value',
#  'margin']
# Shorthand for setting the initial values of widget properties
# While creating a widget, you can set some or all of the initial values of that widget by defining them as keyword arguments in the widget's constructor (as seen below).
# In [12]:
# Text(value='Hello World!', disabled=True)
# Linking two similar widgets
# If you need to display the same value two different ways, you'll have to use two different widgets. Instead of attempting to manually synchronize the values of the two widgets, you can use the traitlet link function to link two properties together. Below, the values of two widgets are linked together.
# In [13]:
# from traitlets import link
# a = FloatText()
# b = FloatSlider()
# display(a,b)
#
# mylink = link((a, 'value'), (b, 'value'))
# Unlinking widgets
# Unlinking the widgets is simple. All you have to do is call .unlink on the link object. Try changing one of the widgets above after unlinking to see that they can be independently changed.
# In [ ]:
# mylink.unlink()
# Conclusion
# You should now be beginning to have an understanding of how Widgets can interact with each other and how you can begin to specify widget details.
