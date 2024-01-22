# PYPER - **Py**thon-Based 3D-**P**rinted **E**lectric **R**over
![pyper](https://i.imgur.com/wx5TQ7o.jpg)
**PYPER** is a **Py**thon-based, 3D-**P**rinted, **E**lectric **R**over. 

I designed PYPER from scratch from the ground up - I used [Blender](https://www.blender.org/) for 3D-modeling of the chassis, steering mechanism, and drivetrain, printed [the parts](https://www.thingiverse.com/thing:6352166) on my [Creality Ender 3 3D Printer](https://www.creality.com/products/ender-3-3d-printer), designed the [electrical circuitry](wiring.drawio), and wrote [the code](./src/) that coordinates its driving mechanics.

The project is fully open source under the [**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International** license](https://creativecommons.org/licenses/by-nc-sa/4.0/). The source code that runs on an onboard Raspberry Pi is available [here](./src/) and the 3D-printed parts (.stl files) can be found [on Thingiverse here](https://www.thingiverse.com/thing:6352166).

### PYPER Specifications
- **Weight**, fully assembled: 23g
- **Dimensions**: 173x213x76 mm (WxLxH)
- **Gear Ratio**: PYPER uses a **48:1** [TT motor](https://www.amazon.com/gp/product/B09N6NXP4H/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) (*please note that, while the title of this product on Amazon states it is a 1:48 ratio, it is actually a 48:1 (reduction) gear ratio*) against a **4:5** 3D-printed compound gear system I developed. [This graphic](https://i.imgur.com/Yiz39RH.png) helped me calculate this ratio:
    - Teeth on motor gear (gear attached to TT motor, receiving rotational input): **15**
    - Teeth on mid-axle gear (intermediary between motor gear and final drive shaft): **24**
    - Teeth on drive shaft gear: **12**
    - Motor Gear to Mid-Axle Gear ratio (driven / driving) = **24/15** = **24:15**
    - Mid-Axle Gear to Drive Shaft Gear ratio (driven / driving) = **12/24** = **12:24**
    - Ratio of **PYPER's 3D-printed** combined gear system = **24/15** * **12/24** = **288/360** = **4/5** = **4:5**
        - This can be interpretted as: *for every 4 turns the motor gear makes (powered by the motor), the final drive shaft will rotate 5 times*.
        - Thus, PYPER's gear system actually *speeds up* the TT motor (gains speed, loses torque) a little bit.
    - Altogether, combining the **48:1** ratio of the TT motor against the **4:5** ratio of PYPER's fixed 3D-printed gear system, PYPER has a **192:5** gear ratio.
        - This means that pairing PYPER's 3D-printed gear system to the TT motor *speeds up* the TT motor slightly, gaining speed, but losing torque (going from gear ratio of **48.0** to **38.4**).

## Why I built PYPER
I built PYPER to demonstrate the essential components required to build a *basic* RC car: a steering mechanism and a mid-mounted motor delivering power to the rear wheels through a multi-gear drivetrain. While many other models you can find online are very impressive, they tend to be overly complex and advanced, posing challenges for beginners to mechanical engineering to understand.

In contrast, PYPER is intentionally designed to be straightforward, accessible, and approachable for *anybody*. So, for the sake of learning, I describe PYPER and its systems (steering, drivetrain, code, etc.) below in detail.

I hope you can learn from PYPER and uses these ideas in your own projects.

## Parts List: What You Need to Build PYPER
PYPER is fully open source, everything you need to build one is available here. These are the parts used in PYPER, if you choose to build a PYPER yourself or repurpose these ideas in your own design:
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

Part costs to build PYPER: **roughly $28.66**.

## PYPER's 3D-Printed Parts Explained
All of the 3D-printed parts needed to make PYPER are available [on Thingiverse](https://www.thingiverse.com/thing:6352166) for free. Each part and its role is described below:
|Image|Part|Function|Role|
|-|-|-|-|
|![img](https://cdn.thingiverse.com/assets/9d/60/7c/95/b9/medium_preview_5398b511-00ff-4f4c-9d4a-e6842469ae3d.png)|base.stl|chassis|The platform everything is built on top of|
|![img](https://cdn.thingiverse.com/assets/f7/66/b3/5b/50/medium_preview_6fd4d756-b786-453c-ac86-6043ff345644.png)|wheel_front.stl|chassis|The two front wheels to the rover. PYPER's design requires two of these.|
|![img](https://cdn.thingiverse.com/assets/f4/13/2c/d6/84/medium_preview_a9383307-72aa-4795-97be-d7945f37b2d2.png)|wheel_rear.stl|chassis|The two rear wheels to the rover. PYPER's design requires two of these.|
|![img](https://i.imgur.com/PHBrIim.png)|hubcap_front.stl|chassis|Hubcap for the front wheels. PYPER's design requires two of these.|
|![img](https://cdn.thingiverse.com/assets/89/0d/0f/c9/be/medium_preview_d2ce201d-1621-40b9-8620-3bc202a74c32.png)|hubcap_rear.stl|chassis|Hubcap for the rear wheels. PYPER's design requires two of these.|
|![img](https://cdn.thingiverse.com/assets/f2/b0/72/a3/81/medium_preview_2abca809-7e6a-4407-85b1-dbd96e63e2d9.png)|steering_upright_right.stl|steering|Mounting the front right wheel to this allows the wheel to "pivot" to accommodate a steering angle, controlled by the servo|
|![img](https://cdn.thingiverse.com/assets/85/64/72/f9/5f/medium_preview_feedb94a-3ae1-473e-a5f9-0aab0a3ab826.png)|steering_upright_left.stl|steering|Mounting the front left wheel to this allows the wheel to "pivot" to accommodate a steering angle, controlled by the servo|
|![img](https://cdn.thingiverse.com/assets/e0/9c/f3/39/af/medium_preview_81367bf7-9a19-407e-b134-6c8cf395163f.png)|tie_rod.stl|steering|Ties the two steering uprights together, mechanically linking them together with the servo, allowing the servo to manipulate the uprights|
|![img](https://cdn.thingiverse.com/assets/1d/8a/d8/64/b7/medium_preview_8304275a-9adf-4cd3-9414-05dd9bf7d918.png)|tt_frame.stl|drivetrain|A frame that fits around the TT motor so it can be mounted to the chassis (base)|
|![img](https://cdn.thingiverse.com/assets/48/66/53/32/fc/medium_preview_249689cf-7534-483e-8abe-a1d6b079cf0a.png)|motor_gear.stl|drivetrain|Fits snuggly around the TT motor's axle, transferring its torque into the drivetrain. PYPER's design requires two of these.|
|![img](https://cdn.thingiverse.com/assets/11/08/12/99/94/medium_preview_d6b55c69-e47a-4c46-98dd-f7671e345f68.png)|mid_axle_gear.stl|drivetrain|Meshes against the **motor_gear.stl**, being driven by the motor gear. PYPER's design requires two of these.|
|![img](https://i.imgur.com/vs2SYBJ.png)|mid_axle.stl|drivetrain|Serves to hold two mid axle gears in place along their axis, allowing them to spin freely. **I recommend printing this at 100% infill to make it stronger**. I have had issues with it snapping at 20% infill.|
|![img](https://cdn.thingiverse.com/assets/01/10/5d/7e/bc/medium_preview_3e8ef466-5e44-4490-94a1-9f52d1d24662.png)|mid_axle_mount.stl|drivetrain|Holds the **mid_axle.stl** in place securely, allowing the mid axle gears to mesh with both the motor gears and drive axle gears. PYPER's design requires two of these.|
|![img](https://i.imgur.com/sJ9wxK4.png)|drive_axle_gear.stl|drivetrain|Meshes against the two **mid_axle_gear.stl**, transfering torque to the final drive, turning the rear wheels. PYPER's design requires two of these.|
|![img](https://cdn.thingiverse.com/assets/1a/ba/19/19/34/medium_preview_6a1d7751-3c5a-47ce-84ba-68fccc894def.png)|drive_axle.stl|drivetrain|Final drive axle. Transfers torque from the two **drive_axle_gear.stl** to the rear wheels, moving the rover forward or backward|
|![img](https://cdn.thingiverse.com/assets/57/f0/64/40/fa/medium_preview_ea64d320-9ecc-4ca9-8326-a7cd56e01cfd.png)|bearing_mount.stl|drivetrain|Holds the **drive_axle.stl** in place, meshing with the two **mid_axle_gear.stl**, and allowing it to spin freely while also supporting the weight of the chassis. PYPER's design requires two of these.|

### Visual Depictions of PYPERS Components
![steering system](https://i.imgur.com/QWwSRlL.png)
![drivetrain: motor mount](https://i.imgur.com/uaLdGjE.png)
![drivetrain: Mid Axle](https://i.imgur.com/G4dgbnp.png)
![drivetrain: Final Drive](https://i.imgur.com/nbxdLVr.png)
These visualizations can be found in [this PowerPoint deck](https://github.com/TimHanewich/PYPER/releases/download/1/visuals.pptx).

### Post-Printing
- You will need to insert a MR115-2RS (5x11x4mm) bearing into the following parts after printing. Each part is designed to accept the bearing with little friction, but you may need to use a mallet/hammer to bang the bearing in.
    - `mid_axle_gear.stl`
    - `bearing_mount.stl`
    - `wheel_front.stl`
- After printing the gears, you may need to slightly sand down some of the teeth of each gear so they mesh well against one another.

## Screwing the 3D-Printed Parts Together
Metric screws are used in PYPER's design due to their wide availability, precision, and compatibility. The holes cut into the 3D-printed parts will fit are all intended for metric screws. 

These are how many of each metric screw specification you'll need:
|Size (width*length)|Count|
|-|-|
|M3*30mm|4|
|M3*12mm|2|
|M3*8mm|4|
|M2*12mm|4|
|M2*8mm|6|
|M2*6mm|2|

These are the specific needs for these screws in PYPER's design:
- 2 M3*30mm for steering uprights
- 2 M3*12mm for steering uprights
- 2 M3*8mm for screwing front wheels in
- 4 M2*12mm for screwing in final drive bearing mounts
- 4 M2*8mm for screwing in mid axle mount
- 2 M3*30mm for screwing TT motor into TT frame
- 2 M3*8mm for screwing TT frame into base
- 2 M2*6mm for screwing in rear wheels
- 2 M2*8mm for screwing in SG90 servo to frame

## Wiring up the Electronics
PYPER uses:
- A **1S (1 cell) Lithium Polymer battery** (but this can be swapped with any battery < 5V that can provide enough current to power these electronics, which is minimal)
- A **MT3608** DC-DC converter to step up the 3.2-4.2 nominal volts of the 1 cell battery to a stable 5V
- An **L293D** brushed DC motor driver for controlling the application of electricity to the motor via the Raspberry Pi's GPIO pins
- A **1:48 gear ratio TT motor** to turn the rear wheels, moving it forward or backward
- An **SG90 servo** to actuate a steering angle
- A **Raspberry Pi Pico W** to serve as "the brain", driving PYPER around according to requests

The components should be wired together as depicted in this wiring diagram below:
![wiring](https://i.imgur.com/gLqn1KU.png)

The draw.io wiring diagram can be found [here](./wiring.drawio), if you'd prefer to pull up a higher-resolution version.

## Driving PYPER: Software
PYPER is drivable via an onboard Raspberry Pi Pico W which runs a web server on your local network and receives movement commands via HTTP requests. PYPER's software is written in **MicroPython** and is available in [the `src` folder here](./src/).

Before deploying this code to your own Raspberry Pi Pico W, you will need to configure a few variables in the [settings.py](./src/settings.py) module:
- `wifi_ssid`: The SSID (username) of your wifi network. The Raspberry Pi Pico will use this to connect to your wifi network and receive movement instructions via HTTP requests.
- `wifi_password`: The password to your wifi network. The Raspberry Pi Pico will use this to connect to your wifi network and receive movement instructions via HTTP requests.
- `gp_steering`: Set this to the GPIO pin (GP number, not pin number) that you are using to control the servo via the servo's signal wire. **If you used the same GP pin that I used in my code, this does not need to be changed**.
- `gp_safety`: Set this to the GPIO pin (GP number, not pin umber) that you have connected to the top-left pin of the L293D motor driver; this serves as the "safety" input (for the L293D to give any power to the motor, this must be set to a high state). **If you used the same GP pin that I used in my code, this does not need to be changed**.
- `gp_i1`: Set this to the GPIO pin (GP number, not pin number) that you are using to control one of the motor inputs (see wiring diagram). **If you used the same GP pin that I used in my code, this does not need to be changed**.
- `gp_i2`: Set this to the GPIO pin (GP number, not pin number) that you are using to control the other motor input (see wiring diagram). **If you used the same GP pin that I used in my code, this does not need to be changed**.

With the contents of the [src folder](./src/) loaded onto a Raspberry Pi Pico W (programs like **Thonny** or **rshell** can be used for this), once the Raspberry Pi Pico W is powered up, it will immediately begin to execute the code in the [main.py](./src/main.py) module. Once the onboard LED of the Raspberry Pi Pico W goes solid, this indicates it is ready to operate!

### Drive Mode
PYPER has two *operation modes*: **HTTP mode** and **UDP mode**. You can change which mode PYPER is in by changing the `operation_mode` variable in the [settings.py](./src/settings.py) module. `0` = HTTP mode, `1` = UDP mode. 

Both operation modes are described in separate documention:
- [Driving PYPER in HTTP mode](./docs/http_mode.md)
- Driving PYPER in UDP mode *(coming soon!)*

## Clips from Development
I routinely took small clips during PYPER's development, demonstrating each part of the design. I'm listing them here for learning purposes, in case you want to study a specific piece:
- [Assembling 3D-printed steering system](https://www.youtube.com/shorts/D8oKYiKBxoA)
- [First demonstration of powered steering system](https://twitter.com/TimHanewich/status/1725139275988021744)
- [First prototype of TT motor mount](https://twitter.com/TimHanewich/status/1726737684020773365)
- [First drivetrain demonstration (no wheels)](https://twitter.com/TimHanewich/status/1729273808488468517)
- [Servo actuating steering angle](https://youtube.com/shorts/jCH9cWKqCqs)
- [Final steering upright design](https://twitter.com/TimHanewich/status/1730002026338066827)
- [Drive axle and mid axle attached to base](https://twitter.com/TimHanewich/status/1730595493309215170)
- [Complete drivetrain Closeup demonstration](https://youtube.com/shorts/8eYT_Qdbzhs)

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