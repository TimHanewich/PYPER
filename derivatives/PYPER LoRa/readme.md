# PYPER LoRa

## Issue on Sept 11, 2024
There is a bizarre issue I encountered.

When the Raspberry Pi Pico was writing specifically a **send** command to the RYLR998, it kept freezing. The REPL via Thonny would freeze but it appeared the program kept running, but much slower.

After a lot of debugging, I eventually figured out that if I lowered the output power of the RYLR998 from 22 (the max) to 12, the problem would go away.