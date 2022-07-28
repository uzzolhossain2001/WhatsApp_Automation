import pyautogui as auto
from time import sleep

while True:
    auto.write('Test automation at 1s intervals')
    auto.press('enter')
    sleep(0.1)
