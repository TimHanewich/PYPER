# Driving PYPER in HTTP Mode
When in **HTTP mode**, you can control PYPER by making HTTP requests to it on your home network. It has several endpoint services you can call to do various things:

### Driving PYPER
You can make an HTTP request to the `/move` endpoint to instruct PYPER to move. PYPER works a lot like NASA's mars rovers: you instruct PYPER to make a maneuver; you specify whether it should move forward or backward, how much power it should move with (throttle), by how much it should be steering to the left or right (steering angle), and how long this maneuver should last. PYPER will execute your instructions, stop, and then response `200 OK` ("that worked successfully!") to you. A request to the `/move` endpoint should look like this:

```
POST /move
Content-Type: application/json

{
    "drive": 0.75,
    "steer": 0.8,
    "duration": 3.0
}
```

In the example above, PYPER will move **forward** at a throttle of **75%**, steering to **the right** at **80%**, and will continue doing so for **3.0** seconds before stopping. Each property explained further:
- `drive`: A value between -1.0 and 1.0. This defines the throttle PYPER will apply to the motor. -1.0 would be 100% throttle in reverse, 1.0 would be 100% throttle forward. 
- `steer`: A value between -1.0 and 1.0. This defines the steering angle PYPER will use when driving (how it is steering).  -1.0 would be 100% steering to the left, 1.0 would be 100% steering to the right.
- `duration`: A value > 0.0. This defines how many **seconds** this specific maneuver should last. 

PYPER also supports movement commands that are **chained together**. For example: 

```
POST /move
Content-Type: application/json

[
    {
        "drive": 0.5,
        "steer": 0.5,
        "duration": 2.0
    },
    {
        "drive": 0.95,
        "steer": -0.5,
        "duration": 2.0
    },
    {
        "drive": -0.4,
        "steer": 0.0,
        "duration": 2.0
    }
]
```

In the above example, PYPER will:
- Drive forward at 50% power and 50% steering angle to the right for 2 seconds.
- Then, drive forward at 95% power and 50% steering angle to the left for 2 seconds.
- Then, drive backward at 40% power with 0% steering angle (straight) for 2 seconds
- Then, return `200 OK` response to the HTTP requestor.

### Status
PYPER can provide a basic status update. This is a good endpoint if you want to "check PYPERS pulse" (see if it is still alive and responding to requests) without moving it. Use the `/status` endpoint like so:

```
GET /status
```

PYPER will respond with the following, as an example:
```
{
    "calls": 6,
    "uptime": 642.623,
    "movements": 2
}
```
Each property in this status payload is described below:
- `calls` - the total number of HTTP requests PYPER has received and responded to. 
- `uptime` - the total number of seconds PYPER has been turned on for (reset each time PYPER loses power).
- `movements` - the total number of individual movement commands (see above) PYPER has received and executed. 

If the user sends a chain request of three movement commands in one call, the `movements` will be incremented by 3 while the `calls` is incremented by 1.

### Disarming PYPER
While PYPER is idling, it is still consuming a marginal amount electricity from the battery to maintain its steering angle (the servo will resist pressure applied that may change the angle). If you'd like to fully disarm PYPER's steering mechanism and onboard motor, you can use the `/disarm` endpoint:

```
GET /disarm
```

PYPER will disarm the servo and terminate any power to the rear wheels .

### Arming PYPER
Once turned on, PYPER is armed and ready to drive. But, if you use the `/disarm` endpoint described above, you will need to re-arm PYPER to get it to start driving again. Use the `/arm` endpoint for doing so:
```
GET /arm
```

After calling to this endpoint and receiving the `200 OK` response, PYPER is ready to drive again.