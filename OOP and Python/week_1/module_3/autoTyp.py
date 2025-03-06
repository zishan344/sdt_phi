import pyautogui 
from time import sleep
i = 0
L = ["PORBO DIGONTE SORGO OTECHE ROKTO LAL LAL ROKTO LAL JOWAR ASESE"]
for i in L:
 sleep(3)
 pyautogui.write(i,interval=0.12)
 pyautogui.press('enter')
 
