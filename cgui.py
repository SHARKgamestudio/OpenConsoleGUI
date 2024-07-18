#•❪❆ by SHARKstudio ❆❫•#

#◥▛▀▀▀▀▀▜ * ▛▀▀▀▀▀▜◤#
#    ConsoleGUILib    #
#◢▙▄▄▄▄▄▟ * ▙▄▄▄▄▄▟◣#


#━━━━━━❪❆❫━━━━━━#


# ◣◤  •IMPORTING MODULES•  ◥◢
import os
import time
import keyboard


# ◣◤  •STATIC FUNCTIONS•  ◥◢
def clear():
    """
        This function clears the content of the console.
        It works on Linux, macOS, and Windows systems, and should also work with some custom IDE consoles.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print("\033[H\033[J", end="")


# ◣◤  •INTERACTIVE MENU•  ◥◢
class MenuStyle:
    """
        This object is used to create custom styles for menus.
    """
    def __init__(self, left_title_border='|[', right_title_border=']|', item_selector='>'):
        self.lt_border = left_title_border
        self.rt_border = right_title_border
        self.item_selector = item_selector

    def get_left_title_border(self):
        """
            This function returns the style decoration for the left side of the title.
            :return: string
        """
        return self.lt_border

    def get_right_title_border(self):
        """
            This function returns the style decoration for the right side of the title.
            :return: string
        """
        return self.rt_border

    def get_item_selector(self):
        """
            This function returns the style decoration for the item selector of the menu.
            :return: string
        """
        return self.item_selector


# predefined styles
im_style0 = MenuStyle('|[', ']|', '>')
im_style1 = MenuStyle('【', '】', '▶')
im_style2 = MenuStyle('☾', '☽', '➤')
im_style3 = MenuStyle('𓇼', '𓇼', '✦')


class MenuItem:
    """
        This object is used for adding items to a menu. You can set up the display text and the trigger function to execute when the item is confirmed.
    """
    def __init__(self, text, trigger):
        self.text = text
        self.trigger = trigger

    def get_text(self):
        return self.text

    def get_trigger(self):
        return self.trigger


class Menu:
    """
        This is the main object used to display interactive menus in the console.
    """
    def __init__(self, title, items, default_selected=0, style=MenuStyle('|[', ']|', '>')):
        self.title = title
        self.items = items
        self.selected = default_selected
        self.style = style
        self.last = self.selected + 1

    def update(self):
        """
            Run this function in a loop to refresh the content of the menu instance.
        """
        # compute inputs
        if keyboard.is_pressed('up'):
            self.selected = self.selected - 1 if self.selected > 0 else 0
        if keyboard.is_pressed('down'):
            self.selected = self.selected + 1 if self.selected < len(self.items) - 1 else len(self.items) - 1
        if keyboard.is_pressed('enter'):
            event_func = self.items[self.selected].get_trigger()
            event_func()

        # display items
        if self.selected != self.last:
            clear()
            print(" " + self.style.get_left_title_border() + self.title + self.style.get_right_title_border() + " ")
            for i in range(len(self.items)):
                select_char = self.style.get_item_selector() + ' ' if i == self.selected else '  '
                print(select_char + " " + str(i) + "." + self.items[i].get_text())
        # update selection
        self.last = self.selected

        # add delay
        time.sleep(0.075)


# ◣◤  •PROGRESS BAR•  ◥◢
class ProgressBarStyle:
    """
        This object is used to create custom styles for progress-bars.
    """
    def __init__(self, empty='▒', filled='█', border=''):
        self.empty = empty
        self.filled = filled
        self.border = border

    def get_empty(self):
        """
            This function returns the style graphic used for displaying the remaining progress.
            :return: string
        """
        return self.empty

    def get_filled(self):
        """
            This function returns the style graphic used for displaying the completed progress.
            :return: string
        """
        return self.filled

    def get_border(self):
        """
            This function returns the style graphic used for the borders of the progress bar on the left and right sides.
            :return: string
        """
        return self.border


# predefined styles
pb_style0 = ProgressBarStyle('▒', '█', '')
pb_style1 = ProgressBarStyle(' ', '█', '|')
pb_style2 = ProgressBarStyle('□', '■', '')
pb_style3 = ProgressBarStyle('▱', '▰', '')


class ProgressBar:
    """
        This is the main object used to display animated progress-bars in the console.
    """
    def __init__(self, length=50, prefix="", display_percent=True, style=ProgressBarStyle('▒', '█', '')):
        self.length = length
        self.prefix = prefix
        self.display_percent = display_percent
        self.style = style
        self.multiplier = 100 / length

    def update(self, value):
        # refresh the console
        clear()

        # get style
        empty = self.style.get_empty()
        filled = self.style.get_filled()
        border = self.style.get_border()

        # prepare vars
        prefix = ' ' + str(self.prefix) + ' ' if self.prefix else ''
        percent = ' ' + str(value) + '%' if self.display_percent else ''
        progress = ''
        remaining = empty * self.length

        # compute progress
        for char in range(int(value / self.multiplier)):
            remaining = remaining.replace(empty, '', 1)
            progress += filled

        # display graphics
        print(prefix + border + progress + remaining + border + percent)
