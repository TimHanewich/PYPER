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
import WeightedAverageCalculator
import BatteryMonitor
import tools
import sys

try:

    f = 1/0

    # boot pattern
    led = machine.Pin("LED", machine.Pin.OUT)
    print("Playing LED boot pattern...")
    for x in range(0, 5):
        led.toggle()
        time.sleep(0.25)

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
    lora_pulse_attempt:int = 0
    while True:
        if lora.pulse:
            break
        else:
            lora_pulse_attempt = lora_pulse_attempt + 1
            print("LoRa not connected after " + str(lora_pulse_attempt) + " attempt. Will try again in a moment...")
            time.sleep(0.5)
        if lora_pulse_attempt >= 10: # if cannot connect to LoRa after 10 attempts, infinite pattern
            while True:
                led.on()
                time.sleep(1)
                led.off()
                led.on()
    print("LoRa connected!")

    # config lora
    print("Configuring LoRa...")
    lora.networkid = 18
    lora.address = 1 # 0 = controller, 1 = rover
    lora.output_power = 22
    lora.band = 960000000 # set band to highest (fastest)
    lora.rf_parameters = (7, 9, 1, 8) # Spreadig Factor of 7, Bandwidth of 500 KHz, Coding Rate of 1, Programmed Preamble of 8
    print("LoRa configured!")

    # config other things
    battery_adc:int = machine.ADC(machine.Pin(settings.gp_battery))
    battery_wac:WeightedAverageCalculator.WeightedAverageCalculator = WeightedAverageCalculator.WeightedAverageCalculator(0.98)
    batmon:BatteryMonitor.BatteryMonitor = BatteryMonitor.BatteryMonitor(BatteryMonitor.PROFILE_18650)

    # infinite loop to handle comms
    led.on()
    operational_status_last_sent:int = time.ticks_ms()
    while True:

        # try to receive message
        print(str(time.ticks_ms()) + " ms: Trying to receive a message...")
        rm:reyax.ReceivedMessage = lora.receive()
        if rm == None:
            print("No message available!")
        else:
            print("A message has been received!")

            # pulse call?
            if bincomms.is_pulse_call(rm.data):
                print("It is a pulse call!")
                print("Sending back pulse echo now...")
                lora.send(rm.address, bytes([bincomms.pulse_echo])) # send back a pulse echo to the address it was received from
            elif bincomms.is_OperationalCommand(rm.data):

                # decode
                print("It was an operational command we received!")
                opcmd = bincomms.OperationalCommand()
                opcmd.decode(rm.data)
                print("OperationalCommand decoded: " + str(opcmd))

                # set drive and steer according to command's wish
                ds.drive(opcmd.throttle)
                ds.steer(opcmd.steer)

            else:
                print("Message with body '" + str(rm.data) + "' received but of unknown format.")

        # time to send out op status?
        if (time.ticks_ms() - operational_status_last_sent) > 8000: # send out every X seconds. Keep in mind this should be lower than the amount of time the LoRaLink controller will wait for a response and then raise the "NO RESP" flag.
            print("It is time to send an operational status!")

            # read battery state of charge (as a percentage)
            vbat_reading:int = battery_adc.read_u16() # read raw
            vbat_reading_smoothed:int = int(battery_wac.feed(float(vbat_reading))) # pass it through a weighted average filter (smooth it out)
            battery_voltage:float = 3.01 + (((vbat_reading_smoothed - 38800) / (54000 - 38800)) * (4.21 - 3.01)) # calculate the voltage on the pin based upon a test of known values (tested reading at 4.2V and reading at 3.0V)
            soc:float = batmon.soc(battery_voltage) # you may be wondering "Well don't you have to un-do the voltage divider?". Normally, yes, we do. But when I laid out the math and did the min/max formula, I was already taking that into account. So therefore, we dont have to here!

            # pack up the response
            opstatus:bincomms.OperationalResponse = bincomms.OperationalResponse()
            opstatus.battery = soc
            print("Sending operational status...")
            lora.send(0, opstatus.encode()) # send to controller
            print("Just sent op status '" + str(opstatus.encode()) + "'!")
            operational_status_last_sent = time.ticks_ms()


        # quick flash and then wait
        led.off() # turn LED off for the short wait period. We just turn it off very briefly here so the user can see the loop is still running.
        time.sleep_ms(100) # wait. But keep in mind that the wait time here must be faster than the speed at which we expect the controller to send messages. Otherwise, they will build up.
        led.on() # turn LED on when running the loop again.

except Exception as e:
    print("FATAL ERROR: " + str(e))
    sys.print_exception(e)
    tools.log_exc(e)
    print("Fatal error has been logged to log.txt")