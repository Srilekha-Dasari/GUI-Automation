"""
PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications. 
The API is designed to be as simple. 
PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3. """
#pip install pyautogui
import pyautogui
print(pyautogui.size()) #displays screen size
print(pyautogui.position())#displays cursor position
# How to get position of the cursor at any point use shortcut F5
print(pyautogui.position())
x = (0, 1919)
y = (0, 1079)
# To move your cursor to a specified position
pyautogui.moveTo(150,100)
# To move your cursor with respect to time duration
pyautogui.moveTo(100,250,duration=5)
#Drag with respect to the present position of the cursor
pyautogui.dragRel(10,10,duration=2)