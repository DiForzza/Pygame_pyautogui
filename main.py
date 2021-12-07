import pyautogui
import psutil

from pywinauto.application import Application
from pywinauto import Desktop

pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

# from imhelper import *

# разрешение экрана 1920 х 1080

# фокусируемся на приложении
try:
    #app = Application(backend="win32").connect(title_re=".*Блокнот")
    app = Application(backend="win32").connect(title_re=".*Resurrected")
    #app.window(title_re='.*Блокнот').set_focus()
    app.window(title_re='.*Resurrected').set_focus()
except:
    app = Application(backend="uia").start('D2R.exe')


def moving():
    pyautogui.moveTo(1920, 1080, duration=1)


def take_screenshot():
    # im = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    super_hp = pyautogui.locateCenterOnScreen('super_hp.png', confidence=0.9)
    pyautogui.moveTo(super_hp)
    print(super_hp)


# если приложение запущенно
def if_proc_is_working():
    for proc in psutil.process_iter():
        name = proc.name()
        # print(name)
        if name == "D2R.exe":
            take_screenshot()

if __name__ == '__main__':
     if_proc_is_working()
