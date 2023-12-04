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

# set up statistics that will be tracked
stat_calls_received:int = 0
stat_movement_commands_executed:int = 0

# start listening
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
led.on()
while True:

    print("Awaiting connection...")
    cl, addr = s.accept()
    print("Connection from " + addr[0] + "!")

    stat_calls_received = stat_calls_received + 1
    
    try:

        # collect bytes
        data = request_tools.read_all(cl, 500)
        print(str(len(data)) + " bytes received")

        if len(data) > 0:
        
            # parse
            req = request_tools.request.parse(data.decode())

            # if it was a move command
            if req.method.lower() == "post" and req.path.lower() == "/move":
                print("Movement command request received!")

                # parse the movement command from the body
                mcs:list[MovementCommand.MovementCommand] = []
                try:
                    mcs = MovementCommand.MovementCommand.parse(req.body)
                except Exception as e:
                    cl.send("HTTP/1.0 400 BAD REQUEST\r\n\r\nThere was an issue parsing the movement commands provided in the body! Msg: " + str(e))
                    cl.close()
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
                    cl.send("HTTP/1.0 400 BAD REQUEST\r\n\r\nThere were validation issues with one or more of the movement commands provided: " + str(validations))
                    cl.close()
                    continue
                print("Movement commands validated!")


                # execute each
                for mc in mcs:
                    if mc != mcs[len(mcs) - 1]: # if it is not the last one
                        ds.execute(mc, False) # do not stop
                    else: # if it is the last one
                        ds.execute(mc, True) # execute it, and then stop, it is the last one
                    stat_movement_commands_executed = stat_movement_commands_executed + 1
                        

                # respond with OK
                cl.send("HTTP/1.0 200 OK\r\n\r\n")
                cl.close()


            elif req.method.lower() == "get" and req.path.lower() == "/status":

                print("It is a status request!")

                # prepare
                ToReturn = {}
                ToReturn["uptime"] = time.ticks_ms() / 1000
                ToReturn["calls"] = stat_calls_received
                ToReturn["movements"] = stat_movement_commands_executed
                ToReturnStr = json.dumps(ToReturn)

                # Return
                cl.send("HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n" + json.dumps(ToReturn))
                cl.close()

            elif req.method.lower() == "get" and req.path.lower() == "/disarm":

                # disable drive + steer
                ds.disable_drive()
                ds.disable_steer()

                # respond with OK
                cl.send("HTTP/1.0 200 OK\r\n\r\n")
                cl.close()

            elif req.method.lower() == "get" and req.path.lower() == "/arm":

                # enable drive + steer
                ds.enable_drive()
                ds.enable_steer()

                # respond with OK
                cl.send("HTTP/1.0 200 OK\r\n\r\n")
                cl.close()



            else:
                print("It was an invalid request")
                cl.send("HTTP/1.0 404 NOT FOUND\r\n\r\n")
                cl.close()

            

        else: # request of 0 bytes (connection?)
            print("Connection with 0 bytes was attempted! Closing...")
            cl.close()  
        
    except Exception as e:
        print("Fatal error! Msg: " + str(e))
        cl.send("HTTP/1.0 500 INTERNAL SERVER ERROR\r\n\r\n")
        cl.close()
        