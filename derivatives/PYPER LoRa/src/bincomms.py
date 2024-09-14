import binary

pulse_call:int = binary.bits_to_byte([True, False, False, False, False, False, False, False]) # Single-byte representation of a pulse call = 128
pulse_echo:int = binary.bits_to_byte([True, True, False, False, False, False, False, False]) # Single-byte representation of a pulse echo = 192

class OperationalCommand:
    def __init__(self) -> None:
        self.throttle:float = 0.0
        self.steer:float = 0.0

    def __repr__(self) -> str:
        return str({"throttle": self.throttle, "steer": self.steer})
    
    def encode(self) -> bytes:
        """Encodes the operational command into a series of two bytes."""
        
        # determine throttle direction
        bit_throttle_direction:bool = False
        if self.throttle >= 0: 
            bit_throttle_direction = True
        else:
            bit_throttle_direction = False

        # determine throttle bits
        throttleabs:float = abs(min(max(self.throttle, -1.0), 1.0))
        throttleval:int = int(throttleabs * 63)
        throttlevalbits:list[bool] = binary.byte_to_bits(throttleval)
        throttle0:bool = throttlevalbits[2]
        throttle1:bool = throttlevalbits[3]
        throttle2:bool = throttlevalbits[4]
        throttle3:bool = throttlevalbits[5]
        throttle4:bool = throttlevalbits[6]
        throttle5:bool = throttlevalbits[7]

        # determine steer direction
        bit_steer_direction:bool = False
        if self.steer >= 0: 
            bit_steer_direction = True
        else:
            bit_steer_direction = False

        # determine steer bits
        steerabs:float = abs(min(max(self.steer, -1.0), 1.0))
        steerval:int = int(steerabs * 63)
        steervalbits:list[bool] = binary.byte_to_bits(steerval)
        steer0:bool = steervalbits[2]
        steer1:bool = steervalbits[3]
        steer2:bool = steervalbits[4]
        steer3:bool = steervalbits[5]
        steer4:bool = steervalbits[6]
        steer5:bool = steervalbits[7]

        # pack!
        byte1:int = binary.bits_to_byte([False, False, bit_throttle_direction, throttle0, throttle1, throttle2, throttle3, throttle4])
        byte2:int = binary.bits_to_byte([throttle5, bit_steer_direction, steer0, steer1, steer2, steer3, steer4, steer5])

        return bytes([byte1, byte2])

    def decode(self, bs:bytes) -> None:
        """Decodes a two-byte sequence into a OperationalCommand."""

        # validate that it is an operational command
        if is_OperationalCommand(bs) == False:
            raise Exception("Provided bytes '" + str(bs) + "' are not a valid OperationalCommand! Cannot decode as one.")
        
        # decode
        b1bits:list[bool] = binary.byte_to_bits(bs[0])
        b2bits:list[bool] = binary.byte_to_bits(bs[1])
        
        # decode throttle
        throttle:int = binary.bits_to_byte([False, False, b1bits[3], b1bits[4], b1bits[5], b1bits[6], b1bits[7], b2bits[0]]) # convert the 6-bits into a value (lead with two empties)
        throttlef:float = throttle / 63 # convert back into float (percent) representation.
        if b1bits[2] == False: # if the direction bit is set to False, this means it is a negative throttle, so multiply by 1
            throttlef = throttlef * -1
        self.throttle = throttlef

        # decode steer
        steer:int = binary.bits_to_byte([False, False, b2bits[2], b2bits[3], b2bits[4], b2bits[5], b2bits[6], b2bits[7]]) # convert the 6-bits into a value (lead with two empties)
        steerf:float = steer / 63 # convert back into float (percent) representation.
        if b2bits[1] == False: # if the direction bit is set to False, this means it is a negative throttle, so multiply by 1
            steerf = steerf * -1
        self.steer = steerf

class OperationalResponse:
    def __init__(self) -> None:
        self.battery:float = 0.0 # battery level, expressed as a percentage

    def __repr__(self) -> str:
        return str({"battery": self.battery})

    def encode(self) -> bytes:
        bat:float = min(max(self.battery, 0.0), 1.0)
        batint:int = int(bat * 63)
        batbits:list[bool] = binary.byte_to_bits(batint)
        byte:int = binary.bits_to_byte([False, True, batbits[2], batbits[3], batbits[4], batbits[5], batbits[6], batbits[7]])
        return bytes([byte])
    
    def decode(self, bs:bytes) -> None:

        # validate that it is an operational response
        if is_OperationalResponse(bs) == False:
            raise Exception("Provided bytes '" + str(bs) + "' is not a valid operational response! Cannot decode as one.")
        
        # convert
        bits:list[bool] = binary.byte_to_bits(bs[0])
        
        # convert to percentage
        batint:int = binary.bits_to_byte([False, False, bits[2], bits[3], bits[4], bits[5], bits[6], bits[7]])
        batf:float = batint / 63
        self.battery = batf

# type checks

def is_pulse_call(data:bytes) -> bool:
    if len(data) != 1:
        return False
    else:
        return data[0] == pulse_call

def is_pulse_echo(data:bytes) -> bool:
    if len(data) != 1:
        return False
    else:
        return data[0] == pulse_echo

def is_OperationalCommand(data:bytes) -> bool:
    sample:bytes = OperationalCommand().encode()
    if len(data) != len(sample):
        return False
    else:
        bits:list[bool] = binary.byte_to_bits(data[0])
        samplebits:list[bool] = binary.byte_to_bits(sample[0]) 
        return bits[0] == samplebits[0] and bits[1] == samplebits[1]
    
def is_OperationalResponse(data:bytes) -> bool:
    sample:bytes = OperationalResponse().encode()
    if len(data) != len(sample):
        return False
    else:
        bits:list[bool] = binary.byte_to_bits(data[0])
        samplebits:list[bool] = binary.byte_to_bits(sample[0]) 
        return bits[0] == samplebits[0] and bits[1] == samplebits[1]