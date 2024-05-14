import pyautogui
import time

while True:
    posicao = pyautogui.position()
    print(posicao)

    time.sleep(1)