#•❪❆ by SHARKstudio ❆❫•#

#◥▛▀▀▀▀▀▜ * ▛▀▀▀▀▀▜◤#
#     progress-demo    #
#◢▙▄▄▄▄▄▟ * ▙▄▄▄▄▄▟◣#


#━━━━━━❪❆❫━━━━━━#

# ◣◤  •IMPORTING MODULES•  ◥◢
from ConsoleGUILib import * # importing 'ConsoleGUILib' for managing progress bars
from time import sleep # importing 'time.sleep' to avoid function stack overflows
import os # importing 'os' to clear the console

#━━━━━━❪❆❫━━━━━━#

os.system("cls") # clear the console just to be cleaner
menu = ConsoleGUILib() # declare a new object of type 'ConsoleGUILib'

#━━━━━━❪❆❫━━━━━━#

for i in range(100): # loop until we reach 100%
    menu.progress_bar("main.py",i) # display the progress bar with the 'name' of the file and the 'value' in percent

for i in range(100): # loop until we reach 100%
    menu.progress_bar("libs.py",i) # display the progress bar with the 'name' of the file and the 'value' in percent
    sleep(0.05) # wait before next iteration for slowing down the progress

for i in range(100): # loop until we reach 100%
    menu.progress_bar("config.yml",i) # display the progress bar with the 'name' of the file and the 'value' in percent

print("finish download !") # display the end of the program