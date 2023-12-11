import socket
import pygame
import time
import datetime
import ControlCommand
import time

# set up pygame controllers
pygame.init()
controllers = []
clock = pygame.time.Clock()
for i in range(0, pygame.joystick.get_count()):
    this_controller = pygame.joystick.Joystick(i)
    print("Detected controller '" + this_controller.get_name() + "'")
    this_controller.init()
    controllers.append(this_controller)

# if no controllers were detected, stop
if len(controllers) == 0:
    print("No connected controllers were detected! Shutting down.")
    exit()

# Final inputs we are tracking
STEER:float = 0.0
LEFT_TRIGGER:float = 0.0
RIGHT_TRIGGER:float = 0.0

# set up socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5.0)

# for tracking and not sending too often
send_every_seconds:float = 0.25
last_sent:float = 0.0 # time, in seconds


while True:
    clock.tick(60)
    for event in pygame.event.get():

        # Handle controller inputs
        if hasattr(event, "axis"):
            if event.axis == 0:
                value:float = float(event.value)
                STEER = value
            elif event.axis == 4:
                value = float(event.value)
                value = (value + 1.0) / 2.0 # convert to range between 0.0 and 1.0
                LEFT_TRIGGER = value
            elif event.axis == 5:
                value = float(event.value)
                value = (value + 1.0) / 2.0 # convert to range between 0.0 and 1.0
                RIGHT_TRIGGER = value
            
    # is it time to send again?
    if (time.time() - last_sent) >= send_every_seconds:
        print("Sending: " + str(STEER) + ", " + str(RIGHT_TRIGGER - LEFT_TRIGGER))
        cc = ControlCommand.ControlCommand()
        cc.steer = max(min(STEER, 1.0), -1.0)
        cc.drive = max(min(RIGHT_TRIGGER - LEFT_TRIGGER, 1.0), -1.0)
        sock.sendto(cc.encode(), ("10.0.0.222", 12000))
        last_sent = time.time()

