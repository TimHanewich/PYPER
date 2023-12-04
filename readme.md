# PYPER - **Py**thon-Based 3D-**P**rinted **E**lectric **R**over
![pyper](https://i.imgur.com/wx5TQ7o.jpg)
**PYPER** is a **Py**thon-based, 3D-**P**rinted, **E**lectric **R**over. 

I designed PYPER from scratch from the ground up - I used [Blender](https://www.blender.org/) for 3D-modeling of the chassis, steering mechanism, and drivetrain, printed [the parts](https://www.thingiverse.com/thing:6352166) on my [Creality Ender 3 3D Printer](https://www.creality.com/products/ender-3-3d-printer), designed the [electrical circuitry](wiring.drawio), and wrote [the code](./src/) that coordinates its driving mechanics

The project is fully open source under the [**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International** license](https://creativecommons.org/licenses/by-nc-sa/4.0/). The source code that runs on an onboard Raspberry Pi is available [here](./src/) and the 3D-printed parts (.stl files) can be found [on Thingiverse here](https://www.thingiverse.com/thing:6352166).

Some more information about PYPER:
- Weigth: 125g?
- Top speed (@ 5V): ?
- Dimensions: 173x213x76 mm (WxLxH)
- Total Cost to build (estimate): $28.66
- Final drive gear ratio: 

## Parts List: What You Need to Build PYPER
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

## PYPER's 3D-Printed Parts Explained
All of the 3D-printed parts needed to make PYPER are available [on Thingiverse](https://www.thingiverse.com/thing:6352166) for free. Each part and its role is described below:
|Image|Part|Function|Role|
|-|-|-|-|
|![img](https://cdn.thingiverse.com/assets/9d/60/7c/95/b9/medium_preview_5398b511-00ff-4f4c-9d4a-e6842469ae3d.png)|base.stl|chassis|The platform everything is built on top of|
|![img](https://cdn.thingiverse.com/assets/f7/66/b3/5b/50/medium_preview_6fd4d756-b786-453c-ac86-6043ff345644.png)|wheel_front.stl|chassis|The two front wheels to the rover|
|![img](https://cdn.thingiverse.com/assets/f4/13/2c/d6/84/medium_preview_a9383307-72aa-4795-97be-d7945f37b2d2.png)|wheel_rear.stl|chassis|The two rear wheels to the rover|
|![img](https://i.imgur.com/PHBrIim.png)|hubcap_front.stl|chassis|Hubcap for the front wheels|
|![img](https://cdn.thingiverse.com/assets/89/0d/0f/c9/be/medium_preview_d2ce201d-1621-40b9-8620-3bc202a74c32.png)|hubcap_rear.stl|chassis|Hubcap for the rear wheels|
|![img](https://cdn.thingiverse.com/assets/f2/b0/72/a3/81/medium_preview_2abca809-7e6a-4407-85b1-dbd96e63e2d9.png)|steering_upright_right.stl|steering|Mounting the front right wheel to this allows the wheel to "pivot" to accomodate a steering angle, controlled by the servo|
|![img](https://cdn.thingiverse.com/assets/85/64/72/f9/5f/medium_preview_feedb94a-3ae1-473e-a5f9-0aab0a3ab826.png)|steering_upright_left.stl|steering|Mounting the front left wheel to this allows the wheel to "pivot" to accomodate a steering angle, controlled by the servo|
|![img](https://cdn.thingiverse.com/assets/e0/9c/f3/39/af/medium_preview_81367bf7-9a19-407e-b134-6c8cf395163f.png)|tie_rod.stl|steering|Ties the two steering uprights together, mechanically linking them together with the servo, allowing the servo to manipulate the uprights|
|![img](https://cdn.thingiverse.com/assets/1d/8a/d8/64/b7/medium_preview_8304275a-9adf-4cd3-9414-05dd9bf7d918.png)|tt_frame.stl|drivetrain|A frame that fits around the TT motor so it can be mounted to the chassis (base)|
|![img](https://cdn.thingiverse.com/assets/48/66/53/32/fc/medium_preview_249689cf-7534-483e-8abe-a1d6b079cf0a.png)|motor_gear.stl|drivetrain|Fits snuggly around the TT motor's axle, transfering its torque into the drivetrain|
|![img](https://cdn.thingiverse.com/assets/11/08/12/99/94/medium_preview_d6b55c69-e47a-4c46-98dd-f7671e345f68.png)|mid_axle_gear.stl|drivetrain|Meshes against the **motor_gear.stl**, being driven by the motor gear|
|![img](https://i.imgur.com/vs2SYBJ.png)|mid_axle.stl|drivetrain|Serves to hold two mid axle gears in place along their axis, allowing them to spin freely|
|![img](https://cdn.thingiverse.com/assets/01/10/5d/7e/bc/medium_preview_3e8ef466-5e44-4490-94a1-9f52d1d24662.png)|mid_axle_mount.stl|drivetrain|Holds the **mid_axle.stl** in place securely, allowing the mid axle gears to mesh with both the motor gears and drive axle gears|
|![img](https://i.imgur.com/sJ9wxK4.png)|drive_axle_gear.stl|drivetrain|Meshes against the two **mid_axle_gear.stl**, transfering torque to the final drive, turning the rear wheels|
|![img](https://cdn.thingiverse.com/assets/1a/ba/19/19/34/medium_preview_6a1d7751-3c5a-47ce-84ba-68fccc894def.png)|drive_axle.stl|drivetrain|Final drive axle. Transfers torque from the two **drive_axle_gear.stl** to the rear wheels, moving the rover forward or backward|
|![img](https://cdn.thingiverse.com/assets/57/f0/64/40/fa/medium_preview_ea64d320-9ecc-4ca9-8326-a7cd56e01cfd.png)|bearing_mount.stl|drivetrain|Holds the **drive_axle.stl** in place, meshing with the two **mid_axle_gear.stl**, and allowing it to spin freely while also supporting the weight of the chassis|

### Visual Depictions
![steering system](https://i.imgur.com/QWwSRlL.png)
![drivetrain: motor mount](https://i.imgur.com/uaLdGjE.png)
![drivetrain: Mid Axle](https://i.imgur.com/G4dgbnp.png)
![drivetrain: Final Drive](https://i.imgur.com/nbxdLVr.png)

### Post-Printing
- You will need to insert a MR115-2RS (5x11x4mm) bearing into the following parts after printing. Each part is designed to accept the bearing with little friction, but you may need to use a mallet/hammer to bang the bearing in.
    - `mid_axle_gear.stl`
    - `bearing_mount.stl`
    - `wheel_front.stl`
- After printing the gears, you may need to slightly sand down some of the teeth of each gear so they mesh well against one another.

## Screwing the 3D-Printed Parts Together
Metric screws are used in PYPER's design due to their wide availability, precision, and compatability. The holes cut into the 3D-printed parts will fit are all intended for metric screws. 

These are how many of each metric screw specification you'll need:
|Size (width*length)|Count|
|-|-|
|M3*30mm|4|
|M3*12mm|2|
|M3*8mm|4|
|M2*16mm|2|
|M2*12mm|4|
|M2*8mm|6|

These are the specific needs for these screws in PYPER's design:
- 2 M3*30mm for steering uprights
- 2 M3*12mm for steering uprights
- 2 M3*8mm for screwing front wheels in
- 4 M2*12mm for screwing in final drive bearing mounts
- 4 M2*8mm for screwing in mid axle mount
- 2 M3*30mm for screwing TT motor into TT frame
- 2 M3*8mm for screwing TT frane into base
- 2 M2*16mm for screwing in rear wheels
- 2 M2*8mm for screwing in SG90 servo to frame

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

## Clips from Development
I routinely took small clips during PYPER's development, demonstrating each part of the design. I'm listing them here for learning purposes, in case you want to study a specific piece:
- [Assembling 3D-printed steering system](https://www.youtube.com/shorts/D8oKYiKBxoA)
- [Drivetrain Closeup demonstration](https://youtube.com/shorts/8eYT_Qdbzhs)
- [Servo actuating steering angle](https://youtube.com/shorts/jCH9cWKqCqs)

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