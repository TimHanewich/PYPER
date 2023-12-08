import struct

class ControlCommand:
    
    def __init__(self) -> None:
        self.frame:int = 0 # frame number
        self.steer:float = 0.0 # between -1.0 and 1.0
        self.drive:float = 0.0 # between -1.0 and 1.0
        

    def encode(self) -> bytes:
        ToReturn:bytearray = bytearray()
        ToReturn.extend(self.frame.to_bytes(4, 'little'))
        ToReturn.extend(struct.pack("f", self.steer))
        ToReturn.extend(struct.pack("f", self.drive))
        return bytes(ToReturn)
    
    def decode(self, _bytes:bytes) -> None:
        self.frame = int.from_bytes(_bytes[0:4], 'little')
        self.steer = struct.unpack("f", _bytes[4:8])[0]
        self.drive = struct.unpack("f", _bytes[8:12])[0]

