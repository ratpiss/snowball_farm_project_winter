from pydirectinput import mouseUp, mouseDown
from pynput import keyboard
from time import sleep
import threading

stop = False

def on_press(key):
    if key == keyboard.Key.end:
        return False #shutting down keyboard listener thread

def farm(): #aiming and shooting
    mouseDown(duration=0, button='right')
    sleep(0.1) #aiming time 
    mouseDown(button='left', duration=0)
    mouseUp(button='left', duration=0)
    mouseUp(button='right', duration=0)

sleep(5) #pause to give you time for opening a game's window
running = True #farming condition 

with keyboard.Listener(on_press=on_press) as listener:
    while running:
        farm()
        if threading.active_count() == 1: #Shutdown if there are only one thread left running
            running = False  
    listener.join()

#Releasing the keys after program is done
mouseUp(button='left', duration=0)
mouseUp(button='right', duration=0)