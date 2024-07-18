from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Tile Position 1: X: 727 Y: 931 RGB: (0,0,0)
# Tile Position 2: X: 887 Y: 931 RGB: (0,0,0)
# Tile Position 3: X: 1035 Y: 931 RGB: (0,0,0)
# Tile Position 4: X: 1174 Y: 931 RGB: (0,0,0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# pyautogui.displayMousePosition()

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(727,931)[0]== 0:
        click(727,931)
    if pyautogui.pixel(887,931)[0]== 0:
        click(887,931)
    if pyautogui.pixel(1035,931)[0]== 0:
        click(1035,931)
    if pyautogui.pixel(1174,931)[0]== 0:
        click(1174,931)

