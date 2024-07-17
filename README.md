
## Usage/Examples

#### Create Menus
Interactive Menus are composed of:
- A title
- A list of items that the user can navigate
- A style that can be applied to change the appearance

Each item contains:
- A text to display
- A function that triggers when the user selects the item and presses the 'enter' key

Here is an example of usage:
```python
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

# Creates a menu with a name and a list of items.
menu = Menu("Sample Menu", items) # You can change the default selected item and apply styles.

# Declare a main loop for running the menu.
while True:
    menu.update()
```

