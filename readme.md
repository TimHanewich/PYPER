# PYPER - Python-Based Printed Electric Rover


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
- software
    - how the code works
    - rover control method (HTTP requests)