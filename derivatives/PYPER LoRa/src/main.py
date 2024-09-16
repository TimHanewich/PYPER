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
import asyncio

async def main():

    try:
        
        # boot pattern
        tools.log("Playing LED boot pattern...")
        led = machine.Pin("LED", machine.Pin.OUT)
        for x in range(0, 5):
            led.toggle()
            await asyncio.sleep_ms(250)

        # start up the Driving system
        tools.log("Initializing DrivingSystem...")
        ds:DrivingSystem.DrivingSystem = DrivingSystem.DrivingSystem()
        ds.enable_drive()
        ds.enable_steer()
        tools.log("Driving system ready!")

        # set up LoRa RYLR998
        tools.log("Setting up LoRa...")
        u = machine.UART(0, tx=machine.Pin(settings.gp_lora_tx), rx=machine.Pin(settings.gp_lora_rx), baudrate=115200)
        lora = reyax.RYLR998(u)
        lora_pulse_attempt:int = 0
        while True:
            if lora.pulse:
                break
            else:
                lora_pulse_attempt = lora_pulse_attempt + 1
                tools.log("LoRa not connected after " + str(lora_pulse_attempt) + " attempt. Will try again in a moment...")
                await asyncio.sleep_ms(500)
            if lora_pulse_attempt >= 10: # if cannot connect to LoRa after 10 attempts, infinite pattern
                while True:
                    led.on()
                    await asyncio.sleep_ms(1000)
                    led.off()
                    await asyncio.sleep_ms(1000)
        tools.log("LoRa connected!")

        # config lora
        tools.log("Configuring LoRa...")
        lora.networkid = 18
        lora.address = 1 # 0 = controller, 1 = rover
        lora.output_power = 12
        lora.band = 960000000 # set band to highest (fastest)
        lora.rf_parameters = (7, 9, 1, 8) # Spreadig Factor of 7, Bandwidth of 500 KHz, Coding Rate of 1, Programmed Preamble of 8
        tools.log("LoRa configured!")

        # config other things
        tools.log("Configuring other things...")
        battery_adc:int = machine.ADC(machine.Pin(settings.gp_battery))
        battery_wac:WeightedAverageCalculator.WeightedAverageCalculator = WeightedAverageCalculator.WeightedAverageCalculator(0.98)
        batmon:BatteryMonitor.BatteryMonitor = BatteryMonitor.BatteryMonitor(BatteryMonitor.PROFILE_18650)

        # define and launch LED blink subroutine
        async def pulse() -> None:
            led.on()
            asyncio.sleep_ms(250)
            led.off()
            asyncio.sleep_ms(250)
        asyncio.create_task(pulse())



        # infinite loop to handle comms
        led.on()
        operational_status_last_sent:int = time.ticks_ms()
        while True:

            # try to receive message
            tools.log("Trying to receive message via UART...")
            rm:reyax.ReceivedMessage = lora.receive()
            tools.log("Message read attempt (UART read) complete!")
            if rm == None:
                tools.log("No message available!")
            else:
                tools.log("A message has been received!")

                # pulse call?
                if bincomms.is_pulse_call(rm.data):
                    tools.log("Message is a pulse call. Sending back pulse echo now...")
                    lora.send(rm.address, bytes([bincomms.pulse_echo])) # send back a pulse echo to the address it was received from
                elif bincomms.is_OperationalCommand(rm.data):

                    tools.log("Message is an operational command!")

                    # decode
                    tools.log("It was an operational command we received!")
                    opcmd = bincomms.OperationalCommand()
                    opcmd.decode(rm.data)
                    tools.log("OperationalCommand decoded: " + str(opcmd))

                    # set drive and steer according to command's wish
                    ds.drive(opcmd.throttle)
                    ds.steer(opcmd.steer)

                else:
                    tools.log("Message with body '" + str(rm.data) + "' received but of unknown format.")

            # time to send out op status?
            tools.log("Checking if time to send operational response...")
            if (time.ticks_ms() - operational_status_last_sent) > 8000: # send out every X seconds. Keep in mind this should be lower than the amount of time the LoRaLink controller will wait for a response and then raise the "NO RESP" flag.
                tools.log("It is time to send an operational status!")

                # read battery state of charge (as a percentage)
                tools.log("Collecting battery reading level...")
                vbat_reading:int = battery_adc.read_u16() # read raw
                vbat_reading_smoothed:int = int(battery_wac.feed(float(vbat_reading))) # pass it through a weighted average filter (smooth it out)
                battery_voltage:float = 3.01 + (((vbat_reading_smoothed - 38800) / (54000 - 38800)) * (4.21 - 3.01)) # calculate the voltage on the pin based upon a test of known values (tested reading at 4.2V and reading at 3.0V)
                soc:float = batmon.soc(battery_voltage) # you may be wondering "Well don't you have to un-do the voltage divider?". Normally, yes, we do. But when I laid out the math and did the min/max formula, I was already taking that into account. So therefore, we dont have to here!

                # pack up the response
                opstatus:bincomms.OperationalResponse = bincomms.OperationalResponse()
                opstatus.battery = soc
                tools.log("Sending operational response...")
                lora.send(0, opstatus.encode()) # send to controller
                tools.log("Just sent op status '" + str(opstatus.encode()) + "'!")
                operational_status_last_sent = time.ticks_ms()

            # wait
            tools.log("Waiting...")
            await asyncio.sleep_ms(100)

    except Exception as e:
        tools.log("FATAL ERROR: " + str(e))
        sys.print_exception(e)
        tools.log_exc(e)
        tools.log("Fatal error has been logged to log.txt")


# run main program!
asyncio.run(main())