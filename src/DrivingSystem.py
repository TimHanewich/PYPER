import settings
import machine
import MovementCommand
import time

class DrivingSystem:

    def __init__(self) -> None:

        # drive train
        self.safety:machine.Pin = machine.Pin(settings.gp_safety, machine.Pin.OUT)
        self.safety.off() # start with safety on
        self.i1:machine.PWM = machine.PWM(machine.Pin(settings.gp_i1, machine.Pin.OUT))
        self.i1.freq(50)
        self.i1.duty_u16(0) # start at 0%
        self.i2:machine.PWM = machine.PWM(machine.Pin(settings.gp_i2, machine.Pin.OUT))
        self.i2.freq(50)
        self.i2.duty_u16(0) # start at 0%

        # steering system
        self.steer_pwm:machine.PWM = None



    ### STEERING SYSTEM BELOW ###
    

    def enable_steer(self) -> None:
        self.steer_pwm = machine.PWM(machine.Pin(settings.gp_steering, machine.Pin.OUT))
        self.steer_pwm.freq(50)
        self.steer(0.0) # to go center
    
    def disable_steer(self) -> None:
        if self.steer_pwm != None:
            self.steer_pwm.deinit() # turn off the PWM
            self.steer_pwm = None

    def steer(self, angle:float) -> None:
        if angle < -1.0 or angle > 1.0:
            raise Exception("Steer angle '" + str(angle) + "' outside of range -1.0 to 1.0")
        if self.steer_pwm != None:
            ns:int = int(round(1500000 + (((2000000 - 1000000) * angle) / 2), 0))
            self.steer_pwm.duty_ns(ns)
    



    #### DRIVE TRAIN SYSTEM BELOW #####


    def enable_drive(self) -> None:
        self.safety.on()
        self.drive(0.0)
    
    def disable_drive(self) -> None:
        self.safety.off()
        self.drive(0.0)

    def drive(self, power:float) -> None:
        duty:int = int(round(65025 * power, 0))
        if power >= 0.0:
            self.i1.duty_u16(0)
            self.i2.duty_u16(duty)
        else:
            self.i1.duty_u16(duty)
            self.i2.duty_u16(0)


    ########### HIGHER LEVEL ##############

    def execute(self, mc:MovementCommand.MovementCommand, stop_at_end:bool = True) -> None:
        self.steer(mc.steer)
        self.drive(mc.drive)
        time.sleep(mc.duration)
        if stop_at_end:
            self.drive(0.0) # stop driving