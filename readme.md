# PYPER - **Py**thon-Based 3D-**P**rinted **E**lectric **R**over
![pyper](https://i.imgur.com/wx5TQ7o.jpg)
**PYPER** is my **Py**thon-based, 3D-**P**rinted, **E**lectric **R**over. I independently designed PYPER from the ground up: mechanical design of the drivetrain and steering mechanism, circuitry for the electronics, and software that runs PYPER.

The project is fully open source. All code is available here. I am working now on listing all of the 3D-printed components on Thingiverse.

## What You Need to Build PYPER
|Part|Cost (USD)|
|-|-|
|~110g of PLA filament (20% infill used)|$1.76|
|1 Raspberry Pi Pico W||
|1 SG-90 Servo Motor||
|1 [TT Motor](https://www.amazon.com/gp/product/B09N6NXP4H/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)|$1.47|
|1 1S Lithium Polymer Battery||
|1 MT3608 DC-DC Boost Converter||
|8 MR115-2RS (5x11x4mm) Bearings||
|1 L293D DC Brushed Motor Driver||
|1 Small Breadboard||
|M2 and M3 Screws, Bolts, Washers||
|Misc Wires||

## Movement Command
```
{
    "drive": 0.5,
    "steer": 0.0,
    "duration": 0.5
}
```
- `drive`: % power to apply, from **1.0** for 100% full forward to **-1.0** for 100% full backward
- `steer`: % steering to apply. from **-1.0** for full left hand steering to **1.0** for full right hand steering
- `duration`: duration this movement command should last for, in seconds (optional)

## To include in project on Thingiverse:
- hardware
    - Total grams of filament used
    - Car weight
    - Car top speed @ 6v?
    - Cost estimate w/ parts and filament
    - All individual parts and full assembled STL
        - And how many of each part you will need to print to make the full thing
    - Video putting it together?
    - What's needed:
        - SG90 servo
        - TT motor
        - a few 5mm bearings.
    - Dimensions
    - Pictures of fully assembled
    - Video of it working
    - Explanation of each part. i.e. compare front + rear hub cap differences
    - Why I made this: basic fundamentals of driving
    - The type of steering system it uses
    - Wiring diagram is supplied as draw.io (and add picture to readme)
- software
    - how the code works
    - rover control method (HTTP requests)