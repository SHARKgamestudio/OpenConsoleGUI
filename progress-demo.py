# It is recommended to import all classes from the library.
from cgui import *

# Creates a progress-bar with a prefix and a specified length (e.g., 25 characters). You can display the % and apply styles.
bar = ProgressBar(length=25)

bar.update(50)