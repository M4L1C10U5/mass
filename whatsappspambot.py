import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(30)
for i in range (10):
    pyautogui.press("y")
    pyautogui.press("o")
    pyautogui.press("0")
    pyautogui.press(" ")
    pyautogui.press("y")
    pyautogui.press("e")
    pyautogui.press("a")
    pyautogui.press("h")
    pyautogui.press("enter")