""" Aim: Automate Mouse """
import pyautogui
#placing cursor at Help button and print its position
#print(pyautogui.position())
# to automate note the cursor position
#pyautogui.moveTo(814,55)
#pyautogui.click() #it works well, it clicks help button


# want to open new file place cursor at that position and note the position
#print(pyautogui.position())
# to automate note the cursor position First find file menu and new file position 
pyautogui.moveTo(27,47,duration=5)
pyautogui.click()
pyautogui.moveTo(40,90,duration=5)
pyautogui.click()
