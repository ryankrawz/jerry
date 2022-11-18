import random
import time

import pyautogui


# Move mouse to random (x,y) coordinate over the course of 1 second
def move_mouse(width, height):
    x_coord = random.randint(1, width)
    y_coord = random.randint(1, height)
    pyautogui.moveTo(x_coord, y_coord, duration = 1)

# Move mouse every 30 seconds
def start_mouse_loop():
    x_size, y_size = pyautogui.size()
    while True:
        move_mouse(x_size, y_size)
        time.sleep(30)

if __name__ == '__main__':
    start_mouse_loop()
