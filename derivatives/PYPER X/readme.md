# PYPER X
Linu**x**-based PYPER

![Raspberry Pi Zero W Pinout](https://i.stack.imgur.com/yHddo.png)

## Using `pigpio` to control PWM on GPIO
- How to install and run daemeon: https://abyz.me.uk/rpi/pigpio/download.html
- https://ben.akrin.com/raspberry-pi-servo-jitter/
    - 0 deg = full left turn
    - 90 deg = straight
    - 180 = full right turn
- http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth

## Setting up PIGPIO to run
First, run `pigpiod` daemeon:
```
sudo pigpiod
```

To ensure it is running:
```
psx aux | grep pigpio
```
You should see it running in there.

## Starting up PYPER X
- Plug in power. Allow it to boot.
- SSH into it.
- Run `pigpiod` daemeon: `sudo pigpiod`
- Confirm `pigpiod` daemeon is running: `psx aux | grep pigpio`
- Run `main.py` with **sudo permissions**: `sudo python main.py`