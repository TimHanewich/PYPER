# Steering system-related GPIO pins. GP #'s, not pin numbers
gp_steering:int = 12

# Drivetrain-related GPIO pins. GP #'s, not pin numbers
gp_safety:int = 13
gp_i1:int = 14
gp_i2:int = 15

# REYAX RYLR998 UART interface
gp_lora_rx:int = 17 # the pin the raspberry pi will use to RECEIVE data to the RYLR998
gp_lora_tx:int = 16 # the pin the raspberry pi will use to SEND data to the RYLR998

# battery ADC
gp_battery:int = 26 # the analog-to-digital pin that will be used to sense the battery state of charge (using a voltage divider)