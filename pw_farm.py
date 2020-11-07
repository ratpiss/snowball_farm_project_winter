from pynput import keyboard
from pynput.mouse import Controller, Button
from time import sleep
import threading

mouse = Controller()

def on_press(key):
    if key == keyboard.Key.end:
        return False #shutting down keyboard listener thread

def farm(): #aiming and shooting
    mouse.press(Button.right)
    sleep(0.2) #aiming time 
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(0.1)
    mouse.release(Button.right)
    sleep(0.2)

sleep(5) #pause to give you time for opening a game's window
running = True #farming condition 

with keyboard.Listener(on_press=on_press) as listener:
    while running:
        farm()
        if threading.active_count() == 1: #Shutdown if there are only one thread left running
            running = False  
    listener.join()

#Releasing the keys after program is done
mouse.release(Button.right)
mouse.release(Button.left)