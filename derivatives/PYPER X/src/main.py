print("Hi, I'm PYPER, your Python-based 3D-Printed Electric Rover!")
print("For more information about PYPER, visit https://github.com/TimHanewich/PYPER")
print("PYPER is available under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license")
print("")

import socket
import json
import time
import request_tools
import RPi.GPIO as GPIO
import MovementCommand
import DrivingSystem

# Set up GPIO
GPIO.setmode(GPIO.BCM) # use GPIO #'s, not pin numbers


# set up driving system
ds = DrivingSystem.DrivingSystem()
ds.enable_drive()
ds.drive(0.0)
ds.steer(0.0)

# Statistics that will be tracked
stat_calls_received:int = 0 # how many HTTP calls have been received
stat_movement_commands_executed:int = 0 # how many movement commands have been executed
start_time:float = time.time() # the time (seconds that this program started). This will be used later to get the uptime (in seconds) of this program.

# Start listening
HOST = "0.0.0.0"
PORT = 80 # HTTP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Binding to host '" + HOST + "' and port '" + str(PORT) + "'...")
s.bind((HOST, PORT))
print("Beginning to listen...")
s.listen(1)
while True:
    print("Now waiting for connection...")
    conn, addr = s.accept()
    print("Connection from " + str(addr) + "!")

    # increment call counter
    stat_calls_received = stat_calls_received + 1

    # get all data
    conn.settimeout(0.5)
    all_data:bytearray = bytearray()
    while True:
        try:
            data:bytes = conn.recv(1024)
            for b in data:
                all_data.append(b)
        except: # there are no more bytes incoming in the stream and the timeout triggered
            break
    print(str(len(all_data)) + " bytes received!")

    # Parse into request
    print("Parsing into request...")
    req:request_tools.request = request_tools.request.parse(all_data.decode())
    print("Request details as follows:")
    print(req.method + " " + req.path)
    print(req.headers)
    print(req.body)

    # HANDLE THE REQUEST HERE!

    if req.method.lower() == "get" and req.path.lower() == "/status":
        payload = {}
        payload["uptime"] = round(time.time() - start_time, 1)
        payload["calls"] = stat_calls_received
        payload["movements"] = stat_movement_commands_executed
        response:str = "HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n" + json.dumps(payload)
        conn.send(response.encode())
        conn.close()
    elif req.method.lower() == "post" and req.path.lower() == "/move":
        print("Movement command request received!")

        # parse from body
        mcs:list[MovementCommand.MovementCommand] = []
        try:
            mcs = MovementCommand.MovementCommand.parse(req.body)
        except Exception as e:
            conn.send(("HTTP/1.0 400 BAD REQUEST\r\n\r\nThere was an issue parsing the movement commands provided in the body! Msg: " + str(e)).encode())
            conn.close()
            continue
        print(str(len(mcs)) + " movement commands received!")

        # validate each movement command
        validations:list[str] = []
        for mc in mcs:
            validation:str = mc.validate()
            if validation != None:
                validations.append(validation)
        if len(validations) > 0:
            print("At least of the movement commands had validation issues!")
            conn.send("HTTP/1.0 400 BAD REQUEST\r\n\r\nThere were validation issues with one or more of the movement commands provided: " + str(validations))
            conn.close()
            continue
        print("Movement commands validated!")

        # execute each
        for mc in mcs:
            if mc != mcs[len(mcs) - 1]: # not the last one
                ds.execute(mc, False) # do not stop at the end
            else:
                ds.execute(mc, True) # stop at the end of it
            stat_movement_commands_executed = stat_movement_commands_executed + 1

        # respond with OK
        conn.send("HTTP/1.0 200 OK\r\n\r\n")
        conn.close()

    else:
        print("It was an invalid request (invalid endpoint service)")
        conn.send("HTTP/1.0 404 NOT FOUND\r\n\r\n".encode())
        conn.close()



