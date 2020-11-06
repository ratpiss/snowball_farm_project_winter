from pydirectinput import mouseUp, mouseDown
from pynput import keyboard
from time import sleep, strftime

stop = False

def on_press(key):
    print(key)
    if key == keyboard.Key.esc:
        return False

def farm():
    mouseDown(duration=0, button='right')
    sleep(0.1)
    mouseDown(button='left', duration=0)
    mouseUp(button='left', duration=0)
    mouseUp(button='right', duration=0)

sleep(5) 

with keyboard.Listener(on_press=on_press) as listener:
    while :
        farm()
    listener.join()


mouseUp(button='left', duration=0)
mouseUp(button='right', duration=0)