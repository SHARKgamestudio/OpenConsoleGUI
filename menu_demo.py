#•❪❆ by SHARKstudio ❆❫•#

#◥▛▀▀▀▀▀▜ * ▛▀▀▀▀▀▜◤#
#     GUI menu-demo    #
#◢▙▄▄▄▄▄▟ * ▙▄▄▄▄▄▟◣#


#━━━━━━❪❆❫━━━━━━#


# ◣◤  •IMPORTING MODULES•  ◥◢
from ConsoleGUILib import * # importing 'ConsoleGUILib' for managing menus
from time import sleep # importing 'time.sleep' to avoid function stack overflows
import os # importing 'os' to clear the console

#━━━━━━❪❆❫━━━━━━#

os.system("cls") # clear the console just to be cleaner
menu = ConsoleGUILib() # declare a new object of type 'ConsoleGUILib'

#━━━━━━❪❆❫━━━━━━#

menu.create_menu("my menu", orientation="vertical") # declare a new menu with the given name & orientation
menu.create_menu_item("First Option",25500) # declare a new option with a unique ID (you can add as much options as you want)
menu.create_menu_item("Second Option",25501) # declare a new option with a unique ID (you can add as much options as you want)
menu.create_menu_item("Third Option",25502) # declare a new option with a unique ID (you can add as much options as you want)
menu.create_menu_item("Quit Program",25503) # declare a new option with a unique ID (you can add as much options as you want)

#━━━━━━❪❆❫━━━━━━#

# uncoment the following lines to test them #

#menu.confirmKey = "f" # change the key to trigger events to "enter"
#menu.downKey = "s" # change the key to navigate downward to "s"
#menu.upKey = "w" # change the key to navigate upward to "w"

#━━━━━━❪❆❫━━━━━━#

menu.draw_menu() # draw the menu a first time on the console

# enter an loop by using recursive function
def loop():
    inputs = menu.checking_inputs() # define 'input' to true if an input is pressed, to refresh the console only when needed
    id = menu.getEvent() # get the id of the element selected (as an int) when the 'confirm' key is pressed

    if(inputs == True): # check if we need to update the console
        menu.draw_menu() # if so, update the console
    sleep(0.1) # wait for secs
    if id == 25503: # if the var 'id' is set with the id of the 'exit' item, stop recursivity
        print("program stopped") # draw a text in the console (or do what-ever action you want)
    else: # if no events as been triggered :
        loop() # just execute the function recursively

loop() # launch the function 'loop' for the first time