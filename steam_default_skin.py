"""
This script will activate all the steam keys, which should be in keys.txt file to your steam library automatically.

Steps:

1. Paste all your keys into file keys.txt (one key per line).
2. Change the path to the folder with pictures.
"""
pictures = 'C:/Users/Vadym/Desktop/steam/pictures'
"""
3. Steam window should be visible in your screen.
4. Run script.
5. Check, if all keys are displaying correctly and press Enter.
6. Wait.
7. DO NOT TOUCH ANYTHING, while script is running!
"""

import pyautogui, time

# open the file with keys
keys = open('keys.txt', 'r')
used_keys = open('used_keys.txt', 'w')

# adding all the keys from file to list
key_list = []

for key in keys:
    key_list.append(key.rstrip())
print (key_list)

# safety measure, make sure that all the keys are displaying correctly
input1 = input("Continue? CTRL+C to BREAK ")

for i in key_list:

    # locating menu
    menu = pyautogui.locateOnScreen(pictures + '/steam_def_add.png')
    mouse1 = pyautogui.center(menu)
    pyautogui.click(mouse1, button='left')
    time.sleep(1)

    # locating activation submenu
    activate = pyautogui.locateOnScreen(pictures + '/steam_def_activate.png')
    mouse2 = pyautogui.center(activate)
    pyautogui.click(mouse2, button='left')
    time.sleep(1)

    pyautogui.press('enter')
    pyautogui.press('enter')

    # using keys from the list to paste into the activation window
    pyautogui.typewrite(i)
    used_keys.write(i)
    used_keys.write("\n")

    pyautogui.press('enter')

    # closing all the unnecessary windows
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')

    # waiting for a new key
    time.sleep(1)
