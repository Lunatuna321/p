import time
from pynput.keyboard import Controller, Listener, Key

keyboard = Controller()
keyboard.press(Key.alt)
keyboard.press(Key.tab)
time.sleep(1)
keyboard.release(Key.alt)
keyboard.release(Key.tab)
