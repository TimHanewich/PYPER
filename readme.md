# PYPER - **Py**thon-Based 3D-**P**rinted **E**lectric **R**over
![pyper](https://i.imgur.com/wx5TQ7o.jpg)
**PYPER** is a **Py**thon-based, 3D-**P**rinted, **E**lectric **R**over. 

I designed PYPER from the ground up - I used [Blender](https://www.blender.org/) for 3D-modeling of the platform, steering mechanism, and drivetrain, printed [these parts]() on my [Creality Ender 3 3D Printer](https://www.creality.com/products/ender-3-3d-printer), designed the [electrical circuitry](wiring.drawio), and wrote [the code](./src/) that coordinates its driving mechanics

The project is fully open source. All code is available here. I am working now on listing all of the 3D-printed components on Thingiverse.

### PYPER Specifications
|Spec|Value|
|-|-|
|Weight|125g?|
|Top Speed (@ 5V)||
|Dimensions|173x213x76 mm (WxLxH)|
|Total Cost to Build|Roughly $28.66|

## What You Need to Build PYPER
|Part|Cost (USD)|
|-|-|
|~110g of [PLA filament](https://www.amazon.com/gp/product/B0BM73MC94/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1) (20% infill used)|$1.76|
|1 [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)|$6|
|1 [SG90 Servo Motor](https://www.amazon.com/Smraza-Helicopter-Airplane-Control-Arduino/dp/B07L2SF3R4/ref=sr_1_5?crid=25A4PZW1IX6Z4&keywords=sg90%2Bservo&qid=1701686041&sprefix=sg90%2Bse%2Caps%2C111&sr=8-5&th=1)|$1.88|
|1 [TT Motor](https://www.amazon.com/gp/product/B09N6NXP4H/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)|$1.47|
|1 [1S Lithium Polymer Battery](https://www.amazon.com/gp/product/B07L9SHHFX/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)|$6.42|
|1 [MT3608 DC-DC Boost Converter](https://www.amazon.com/Converter-Adjustable-Voltage-Regulator-Compatible/dp/B089JYBF25/ref=sr_1_3?crid=FGQJZDRRPHZN&keywords=mt3608&qid=1701686153&sprefix=mt3608%2Caps%2C96&sr=8-3)|$0.90|
|8 [MR115-2RS (5x11x4mm) Bearings](https://www.amazon.com/gp/product/B07X6DK946/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)|$4.27|
|1 [L293D DC Brushed Motor Driver](https://www.amazon.com/gp/product/B077TY21T7/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1)|$1.25|
|1 [Small Breadboard](https://www.amazon.com/gp/product/B07LFD4LT6/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)|$1.71|
|22 [M2 and M3 Screws, Bolts, Washers (see below)](https://www.amazon.com/gp/product/B07FCDL2SY/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1)|< $2.00|
|Misc Wires|< $1.00|

## PYPER's Parts Explained
Parts are provided [on Thingiverse]() as STL files. Each part and its role is described below:
|Image|Part|Function|Role|
|-|-|-|-|
|![img]()|base.stl|chassis|The platform everything is built on top of|
|![img]()|wheel_front.stl|chassis|The two front wheels to the rover|
|![img]()|wheel_rear.stl|chassis|The two rear wheels to the rover|
|![img]()|hubcap_front.stl|chassis|Hubcap for the front wheels|
|![img]()|hubcap_rear.stl|chassis|Hubcap for the rear wheels|
|![img]()|steering_upright_right.stl|steering|Mounting the front right wheel to this allows the wheel to "pivot" to accomodate a steering angle, controlled by the servo|
|![img]()|steering_upright_left.stl|steering|Mounting the front left wheel to this allows the wheel to "pivot" to accomodate a steering angle, controlled by the servo|
|![img]()|tie_rod.stl|steering|Ties the two steering uprights together, mechanically linking them together with the servo, allowing the servo to manipulate the uprights|
|![img]()|tt_frame.stl|drivetrain|A frame that fits around the TT motor so it can be mounted to the chassis (base)|
|![img]()|motor_gear.stl|drivetrain|Fits snuggly around the TT motor's axle, transfering its torque into the drivetrain|
|![img]()|mid_axle_gear.stl|drivetrain|Meshes against the **motor_gear.stl**, being driven by the motor gear|
|![img]()|mid_axle.stl|drivetrain|Serves to hold two mid axle gears in place along their axis, allowing them to spin freely|
|![img]()|mid_axle_mount.stl|drivetrain|Holds the **mid_axle.stl** in place securely, allowing the mid axle gears to mesh with both the motor gears and drive axle gears|
|![img]()|drive_axle_gear.stl|drivetrain|Meshes against the two **mid_axle_gear.stl**, transfering torque to the final drive, turning the rear wheels|
|![img]()|drive_axle.stl|drivetrain|Final drive axle. Transfers torque from the two **drive_axle_gear.stl** to the rear wheels, moving the rover forward or backward|
|![img]()|bearing_mount.stl|drivetrain|Holds the **drive_axle.stl** in place, meshing with the two **mid_axle_gear.stl**, and allowing it to spin freely while also supporting the weight of the chassis|


## Screws Needed to Put it all together
- 2 M3*30mm for steering upright
- 2 M3*12mm for steering upright
- 2 M3*8mm for screwing front wheels in
- 4 M2*12mm for screwing in final drive bearing mounts
- 4 M2*8mm for screwing in mid axle mount
- 2 M3*30mm for screwing TT motor into frame
- 2 M3*8mm for screwing into TT frame into body
- 2 M2*16mm for screwing in rear wheels
- 2 M2*8mm for screwing in SG90 servo to frame

|Size|Count|
|-|-|
|M3*30mm|4|
|M3*12mm|2|
|M3*8mm|4|
|M2*16mm|2|
|M2*12mm|4|
|M2*8mm|6|

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
    - ~~Total grams of filament used~~
    - ~~Car weight~~
    - ~~Car top speed @ 6v?~~
    - ~~Cost estimate w/ parts and filament~~
    - All individual parts and full assembled STL
        - And how many of each part you will need to print to make the full thing
    - Video putting it together?
    - ~~Dimensions~~
    - ~~Pictures of fully assembled~~
    - Video of it working
    - Explanation of each part. i.e. compare front + rear hub cap differences
    - Why I made this: basic fundamentals of driving
    - The type of steering system it uses
    - Wiring diagram is supplied as draw.io (and add picture to readme)
- software
    - how the code works
    - rover control method (HTTP requests)