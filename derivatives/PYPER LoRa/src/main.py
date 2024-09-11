print("Hi, I'm PYPER LoRa, your Python-based 3D-Printed Electric Rover!")
print("For more information about PYPER, visit https://github.com/TimHanewich/PYPER")
print("PYPER is available under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license")
print("")

import machine
import time
import DrivingSystem

# boot pattern
led = machine.Pin("LED", machine.Pin.OUT)
print("Playing LED boot pattern...")
for x in range(0, 5):
    led.toggle()
    time.sleep(0.25)
led.on()

# start up the Driving system
print("Initializing DrivingSystem...")
ds:DrivingSystem.DrivingSystem = DrivingSystem.DrivingSystem()
ds.enable_drive()
ds.enable_steer()

