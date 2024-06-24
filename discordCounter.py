import time
from pynput.keyboard import Controller, Listener, Key

keyboard = Controller()

keyboard.press(Key.cmd)
keyboard.press(Key.tab)
keyboard.press(Key.right)
time.sleep(0.8)

keyboard.release(Key.right)


keyboard.release(Key.cmd)
keyboard.release(Key.tab)
