![Logo](https://zupimages.net/up/23/02/npog.png)

# OpenConsoleGUI

✧ Interactive Console Menus & Loading Bars ✧

❱ Open Console GUI is a library for easily creating interactive terminal GUIs with minimal code.
## Installation

OpenConsoleGUI can be installed from pypi using pip:
```bash
pip install open-console-gui
```

Or it can be cloned from GitHub if you want, for example to edit the package:
```bash
git clone https://github.com/SHARKgamestudio/OpenConsoleGUI.git
```
## Features

- Interactive menus with keyboard navigation
- Predefined / custom styles for menus
- Interactive progress-bars with a ton of options
- Predefined / custom styles for progress-bars

↻ More Features are planned for future updates.
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

#### Create Progress-Bars
Progress-Bars are composed of:
- A prefix
- A length (in char)
- A style that can be applied to change the appearance

Here is an example of usage:
```python
# It is recommended to import all classes from the library.
from cgui import *

# Creates a progress-bar with a prefix and a specified length (e.g., 25 characters).
bar = ProgressBar(prefix="myBar", length=25) # You can display the % and apply styles.

# Create a loop for updating the value (must be given in %).
for progress in range(100):
    bar.update(progress + 1)
```
## Using Styles
❱ Styles let you customize the appearance of console GUI elements.

❱ There are two ways to stylize your elements:

- Predefined Styles
- Custom Styles

#### Predefined Styles
OpenConsoleGUI comes with pre-packaged styles for both menus and progress-bars.

Use them by referencing their variable names in the constructor of your GUI element:
```python
menu = Menu("Sample Menu", items, style=im_style0)
```
-- --
➮ Here are all the pre-packaged styles available:

im_style_0 :
```
 |[Sample Menu]|
>  0.Item0
   1.Item1
   2.Item2
```

im_style_1 :
```
 【Sample Menu】
▶  0.Item0
   1.Item1
   2.Item2
```

im_style_2 :
```
 ☾Sample Menu☽
➤ 0.Item0
   1.Item1
   2.Item2
```

im_style_3 :
```
 𓇼Sample Menu𓇼
✦  0.Item0
   1.Item1
   2.Item2
```

pb_style_0 :
```
████████████············ 50%
```

pb_style_1 :
```
|████████████             | 50%
```

pb_style_2 :
```
■■■■■■■■■■■■□□□□□□□□□□□□□ 50%
```

pb_style_3 :
```
▰▰▰▰▰▰▰▱▱▱▱▱▱ 50%
```

#### Custom Styles
❱ You can create custom styles by using the appropriate class for your GUI element.

❱ You can apply them the same way as the predefined ones.

➮ Here is an example with MenuStyle:
```python
myStyle = MenuStyle('☾', '☽', '➤')
menu = Menu("Sample Menu", items, style=myStyle)
```

➮ Here is an example with ProgressBarStyle:
```python
myStyle = ProgressBarStyle('□', '■', '')
menu = ProgressBar(length=25, style=myStyle)
```
## Credits

This library uses the modules 'os', 'time', and 'keyboard'.

['keyboard' by BoppreH](https://pypi.org/project/keyboard/)
