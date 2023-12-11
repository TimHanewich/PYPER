# Wifi Network credentials
wifi_ssid = ""
wifi_password = ""

# Steering system-related GPIO pins. GP #'s, not pin numbers
gp_steering:int = 12

# Drivetrain-related GPIO pins. GP #'s, not pin numbers
gp_safety:int = 13
gp_i1:int = 14
gp_i2:int = 15

# Operation Mode
# 0 = HTTP-based. You will send HTTP requests to PYPER to instruct it to move at a specific power level with a specific steering angle for a specific duration. (default)
# 1 = UDP-based. You will continuously broadcast packets over UDP. PYPER will receive these and adjust its steering angle and power accordingly.
operation_mode:int = 0