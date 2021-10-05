import pyautogui
from PIL import ImageGrab
while True:
    if (pyautogui.locateOnScreen("1.png", grayscale=True, confidence=0.7) is not None):
        pyautogui.click(pyautogui.locateOnScreen("1.png", grayscale=False, confidence=0.7))
    if (pyautogui.locateOnScreen("2.png", grayscale=True, confidence=0.7) is not None):
        pyautogui.click(pyautogui.locateOnScreen("2.png", grayscale=False, confidence=0.7))
