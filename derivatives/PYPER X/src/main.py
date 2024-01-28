print("Hi, I'm PYPER, your Python-based 3D-Printed Electric Rover!")
print("For more information about PYPER, visit https://github.com/TimHanewich/PYPER")
print("PYPER is available under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license")
print("")

import socket
import json
import time
import request_tools
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM) # use GPIO #'s, not pin numbers


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
    else:
        print("It was an invalid request (invalid endpoint service)")
        conn.send("HTTP/1.0 404 NOT FOUND\r\n\r\n".encode())
        conn.close()



