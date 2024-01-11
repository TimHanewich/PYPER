import struct

class ControlCommand:
    
    def __init__(self) -> None:
        self.steer:float = 0.0 # between -1.0 and 1.0
        self.drive:float = 0.0 # between -1.0 and 1.0
        

    def encode(self) -> bytes:
        ToReturn:bytearray = bytearray()
        ToReturn.extend(struct.pack("f", self.steer))
        ToReturn.extend(struct.pack("f", self.drive))
        return bytes(ToReturn)
    
    def decode(self, _bytes:bytes) -> None:
        self.steer = struct.unpack("f", _bytes[0:4])[0]
        self.drive = struct.unpack("f", _bytes[4:8])[0]

