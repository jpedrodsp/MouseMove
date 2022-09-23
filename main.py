import logging
import random as randlib
import pyautogui

def mouseThud():
    mx, my = pyautogui.size()
    ox, oy = pyautogui.position()
    x, y = randlib.randint(0, mx), randlib.randint(0, my)
    pyautogui.moveTo(x, y)
    pyautogui.moveTo(ox, oy)
    logging.info(f"Applied MouseThud: {x}, {y} -> {ox}, {oy}")
    return

def volumeThud():
    pyautogui.keyDown("volumeup")
    pyautogui.keyUp("volumeup")
    pyautogui.keyDown("volumedown")
    pyautogui.keyUp("volumedown")
    logging.info(f"Applied VolumeThud")
    return

def choose_random_function():
    candidates = [mouseThud, volumeThud]
    return randlib.choice(candidates)

def application_lifecycle():
    # Configure logging
    logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG)
    while True:
        f = choose_random_function()
        f()
    return 

if __name__ == "__main__":
    application_lifecycle()