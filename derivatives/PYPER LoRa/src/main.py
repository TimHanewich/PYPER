print("Hi, I'm PYPER LoRa, your Python-based 3D-Printed Electric Rover!")
print("For more information about PYPER, visit https://github.com/TimHanewich/PYPER")
print("PYPER is available under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license")
print("")

import machine
import time
import DrivingSystem
import reyax
import bincomms
import settings

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
print("Driving system ready!")

# set up LoRa RYLR998
print("Setting up LoRa...")
u = machine.UART(0, tx=machine.Pin(settings.gp_lora_tx), rx=machine.Pin(settings.gp_lora_rx), baudrate=115200)
lora = reyax.RYLR998(u)
while True:
    if lora.pulse:
        break
    else:
        print("LoRa not connected. will try again in a moment...")
        time.sleep(1.5)
print("LoRa connected!")

