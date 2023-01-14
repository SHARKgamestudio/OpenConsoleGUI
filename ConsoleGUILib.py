#•❪❆ by SHARKstudio ❆❫•#

#◥▛▀▀▀▀▀▜ * ▛▀▀▀▀▀▜◤#
#     ConsoleGUILib    #
#◢▙▄▄▄▄▄▟ * ▙▄▄▄▄▄▟◣#


#━━━━━━❪❆❫━━━━━━#


# ◣◤  •IMPORTING MODULES•  ◥◢
import os # importing 'os' package for refreshing the console
import keyboard # importing 'keyboard' package for getting keys inputs

class ConsoleGUILib(): # defining main class
    def __init__(self): # init main class
        # Menu Data
        self.menuTitle = "" # the title of the next menu to be drawn
        self.menu_orientation = "" # orientation of the next menu to be drawn (should be "vertical" or "horizontal")
        self.menu_items = [] # list the differents id's of the next menu to be drawn
        self.items_lbl = [] # list the differents labels of the next menu to be drawn
        self.selectedIndex = 0 # represent the actual item index selected on the next menu_items list

        # Input Config
        self.upKey = "up" # the "up" navigation key for menus (can be changed at runtime)
        self.downKey = "down" # the "down" navigation key for menus (can be changed at runtime)
        self.confirmKey = "space" # the key for triggering events (can be changed at runtime)

    # ◣◤  •MAIN FUNCTIONS•  ◥◢

    # Function for creating a menu title.
    def create_menu(self, label="", orientation="vertical"): # WARNING 'orientation' should be "vertical" or "horizontal" otherwize you will get an error
        """create a menu with the given 'label', the 'orientation' set the way 'items' are organyized."""
        self.menuTitle = label # assigning var with parametter passed to the function
        if orientation == "vertical" or orientation == "horizontal": # checking if the 'orientation' parametter as been correctly set
            self.menu_orientation = orientation # if so, assigning the var with parametter passed to the function
        else:
            print("ERROR : {" + orientation + "} is not a valid type of menu_orientation.") # if not, displaying error into the console

    # Function for calling new menu item (id is used for getting events).
    def create_menu_item(self, label="",id=0): # the 'id' is important, please fill it with a "UNIQUE" number
        """create a new item in the menu, 'label' is used for display and 'id' to trigger events."""
        self.menu_items.append(id) # adding 'id' to the end of the list
        self.items_lbl.append(label) # adding 'label' to the end of the list

    # Function for checking inputs (used for knowing when refreshing the console).
    def checking_inputs(self): # please dont pass anny parametter here
        """check the inputs and return 'True' if a key is pressed."""
        if keyboard.is_pressed(self.downKey): # cheking if we press down
            if self.selectedIndex < len(self.menu_items) - 1: # checking if the var does not get of the range of the list
                self.selectedIndex += 1 # if so, adding 1 to the var
                return True # return that an input as been pressed
            else:
                self.selectedIndex = 0 # if not, reset the var to 0
                return True # return that an input as been pressed
        elif keyboard.is_pressed(self.upKey): # cheking if we press up
            if self.selectedIndex > 0: # checking if the var does not get of the range of the list
                self.selectedIndex -= 1 # if so, delete 1 from the var
                return True # return that an input as been pressed
            else:
                self.selectedIndex = len(self.menu_items) - 1 # if not, reset the var to the listLenght - 1
                return True # return that an input as been pressed
        else:
            return False # if we are not pressing anny key, return false; because we dont want to refresh the console
    
    # Function for calling the menu in the console.
    def draw_menu(self): # please dont pass anny parametter here
        """simple function that just display the menu and items in the console."""
        i=0 # init a new int called "i"
        os.system("cls") # refresh the console
        print("[" + self.menuTitle + "]\n") # print the title with some decorations
        for i in range(len(self.menu_items)): # do for the number of elements in the list
            if(self.selectedIndex == i): # check if the element is selected
                print(">" + str(i) + "| " + str(self.items_lbl[i])) # if so, print an arrow before the element
            else:
                print(str(i) + "| " + str(self.items_lbl[i])) # if not, just print the element

    # Function for checking witch menu_item is selected before proceeding.
    def getEvent(self): # please dont pass anny parametter here
        """if the event is triggered, return the item 'id' actualy selected."""
        if keyboard.is_pressed(self.confirmKey): # check if we are pressing the key to trigger the event
            return self.menu_items[self.selectedIndex] # if so return the "id" of the actual selected element

    # Function to draw progress bar (like pip ones) in console (value should be geven in %).
    def progress_bar(self, fileName="", value=100): # you can leave the 'fileName' blank, but please give the 'value' IN PERCENT (%)
        """draw a progress_bar in the console with the given 'value' in % and the given 'fileName'."""
        os.system("cls") # refresh the console
        char = "" # init a new string
        spaces = "                                                  " # init a new string with 50 spaces
        i = 0 # init a new int
        while i < value: # do until we come across the 'value'
            char += "█" # add one '█' char to the string
            spaces = spaces.replace(' ', '', 1) # took of one space from the string to let the end of the bar at the same position
            i += 2 # add 2 to i (so the bar will take 50 caracters instead of 100 wich is to long)
        print(fileName + " |" + char + spaces + "| " + str(value) + "%") # print the final result with the 'fileName' + grahical part of the bar + precise percentage