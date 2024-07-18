# It is recommended to import all classes from the library.
from cgui import *


# Declare functions triggered by items.
def event0():
    # do something
    pass
def event1():
    # do something
    pass
def event2():
    # do something
    pass

# Declare items with names and associated trigger functions executed upon confirmation events.
items = [
    MenuItem("Item0", event0),
    MenuItem("Item1", event1),
    MenuItem("Item2", event2)
]

# Creates a menu with a name and a list of items. You can change the default selected item and apply styles.
menu = Menu("Sample Menu", items)

# Create a main loop for running the menu.
while True:
    menu.update()
