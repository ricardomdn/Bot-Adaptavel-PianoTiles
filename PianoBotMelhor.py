import win32gui
import win32api
import win32con
import time
import keyboard

def pegarCorPixel(x, y):
    hd = win32gui.GetDC(0)
    cor = win32gui.GetPixel(hd, x, y)
    win32gui.ReleaseDC(0, hd)
    return cor

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


coordenadas = [
    (500, 254),
    (598, 254),
    (711, 254),
    (804, 254),
    (500, 366),
    (598, 366),
    (711, 366),
    (804, 366),
    (500, 461),
    (598, 461),
    (711, 461),
    (804, 461),
    (500, 556),
    (598, 556),
    (711, 556),
    (804, 556),
]

preto = 0x000000

while keyboard.is_pressed('p') == False:
    for coord in coordenadas:
        cor_pixel = pegarCorPixel(*coord)
        if cor_pixel == preto:
            click(coord[0], coord[1])
