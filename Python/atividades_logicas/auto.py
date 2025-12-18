import pyautogui
import time

pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("https://ge.globo.com/")
pyautogui.press("enter")
