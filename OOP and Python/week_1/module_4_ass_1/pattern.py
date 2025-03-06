import pyautogui
import time

t = input()
time.sleep(5)
pyautogui.write(t)
pyautogui.press('enter')
for i in range(int(t)):
    for j in range(i + 1):
        pyautogui.write("#") 
    pyautogui.press("enter") 
