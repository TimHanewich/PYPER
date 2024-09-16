import time
import machine

u = machine.UART(0, tx=machine.Pin(16), rx=machine.Pin(17), baudrate=115200)
#u = machine.UART(1, tx=machine.Pin(4), rx=machine.Pin(5), baudrate=115200)

print("First read: " + str(u.read()))

# write
u.write("AT\r\n")
time.sleep(0.25)
print("Read after AT #1: " + str(u.read()))

# write
u.write("AT\r\n")
time.sleep(0.25)
print("Read after AT #2: " + str(u.read()))

# write
u.write("AT\r\n")
time.sleep(0.25)
print("Read after AT #3: " + str(u.read()))

# set band
u.write("AT+BAND=960000000\r\n")
time.sleep(0.25)
print("Set band: " + str(u.read()))

# set output power
u.write("AT+CRFOP=8\r\n")
time.sleep(0.25)
print("Set output power: " + str(u.read()))

# Band
u.write("AT+BAND?\r\n")
time.sleep(0.25)
print("Band: " + str(u.read()))

# RF params
u.write("AT+PARAMETER?\r\n")
time.sleep(0.25)
print("RF Params: " + str(u.read()))

while True:

    print("Next loop @ " + str(time.ticks_ms()))
    
    # write
    print("Writing send...")
    u.write("AT+SEND=2,5,hello\r\n")
    time.sleep(1.0)

    # wait
    #print("Waiting...")
    
    # read
    print("Reading...")
    print(u.read())
    print("Read complete!")

    # wait
    time.sleep(0.25)