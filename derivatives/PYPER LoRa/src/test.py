import time
import machine

u = machine.UART(0, tx=machine.Pin(16), rx=machine.Pin(17), baudrate=115200)

u.write("AT\r\n")
time.sleep(0.1)
u.read()

led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.on()
    u.write("AT+SEND=2,5,hello\r\n")
    print(str(time.ticks_ms()) + ": " + str(u.read()))
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    

