print("Hi, I'm PYPER, your Python-based 3D-Printed Electric Rover!")
print("For more information about PYPER, visit https://github.com/TimHanewich/PYPER")
print("PYPER is available under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license")
print("")

import machine
import network
import socket
import json
import time
import request_tools
import settings
import MovementCommand
import DrivingSystem
import json
import ControlCommand

# boot pattern
led = machine.Pin("LED", machine.Pin.OUT)
print("Playing LED boot pattern...")
for x in range(0, 5):
    led.toggle()
    time.sleep(0.25)
led.on()

# connect to wifi network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
while wlan.isconnected() == False:
    # blip light
    led.on()
    time.sleep(0.1)
    led.off()
    
    print("Attemping to connect to wifi...")
    wlan.connect(settings.wifi_ssid, settings.wifi_password)
    time.sleep(3)
print("Connected to wifi!")
my_ip:str = str(wlan.ifconfig()[0])
print("My IP Address: " + my_ip)

# start up the Driving system
ds:DrivingSystem.DrivingSystem = DrivingSystem.DrivingSystem()
ds.enable_drive()
ds.enable_steer()




# start listening
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 12000))
print("Now listening for incoming UDP messagins on IP '" + my_ip + "' on port 12000")
led.on()
while True:

    print("Awaiting UDP message @ " + str(time.ticks_ms()) + " ticks")
    msg,addr = s.recvfrom(1024)
    print("Connection from " + str(addr) + " of length " + str(len(msg)))

    if len(msg) == len(ControlCommand.ControlCommand().encode()): # it is a control command
        print("Control command received!")

        # decode
        cc = ControlCommand.ControlCommand()
        cc.decode(msg)
        print("CC: steer[" + str(cc.steer) + "] drive[" + str(cc.drive) + "]")

        # execute
        ds.steer(cc.steer)
        ds.drive(cc.drive)
        