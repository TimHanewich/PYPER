import pigpio
import RPi.GPIO as GPIO
import time
import MovementCommand
import settings

class DrivingSystem:

    def __init__(self) -> None:

        # setup GPIO's for drive
        GPIO.setup(settings.gpio_drive_safety, GPIO.OUT)
        GPIO.setup(settings.gpio_drive_i1, GPIO.OUT)
        GPIO.setup(settings.gpio_drive_i2, GPIO.OUT)

        # setup PWM, using RPi.GPIO, for drive
        self.i1 = GPIO.PWM(settings.gpio_drive_i1, 50)
        self.i2 = GPIO.PWM(settings.gpio_drive_i2, 50)
        self.i1.start(0.0) # start at 0% duty cycle
        self.i2.start(0.0) # start at 0% duty cycle

    def enable_drive(self) -> None:
        GPIO.output(settings.gpio_drive_safety, GPIO.HIGH)

    def disable_drive(self) -> None:
        GPIO.output(settings.gpio_drive_safety, GPIO.LOW)
    
    def drive(self, power:float) -> None:
        power = max(min(power, 1.0), -1.0) # constrain within bounds
        if power >= 0.0:
            self.i1.ChangeDutyCycle(power)
            self.i2.ChangeDutyCycle(0.0)
        else:
            self.i1.ChangeDutyCycle(0.0)
            self.i2.ChangeDutyCycle(power * -1)


