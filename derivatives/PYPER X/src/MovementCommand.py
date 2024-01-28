import json

class MovementCommand:
    def __init__(self) -> None:
        self.drive:float = 0.0 # drive power, -1.0 to 1.0
        self.steer:float = 0.0 # steering angle, -1.0 to 1.0
        self.duration:float = 0.0 # time, in seconds

    def validate(self) -> str:

        problems:list[str] = []

        if self.drive < -1.0 or self.drive > 1.0:
            problems.append("drive must be between 0.0 and 1.0")
        
        if self.steer < -1.0 or self.steer > 1.0:
            problems.append("steer must be between -1.0 and 1.0")
        
        if self.duration < 0.0:
            problems.append("duration must be > 0.0")
        
        if len(problems) > 0: # if there were problems, append them to a string and return
            ToReturn:str = ""
            for problem in problems:
                ToReturn = ToReturn + problem + ", "
            ToReturn = ToReturn[0:-2]
            return ToReturn
        else: # if there were no problems, retur None
            return None
        
    @staticmethod
    def parse(json_string:str) -> list["MovementCommand"]:
        """Parses a single or multiple JSON-serialized MovementCommand and returns as a list"""

        deserialized = json.loads(json_string)

        ToReturn:list["MovementCommand"] = []

        if isinstance(deserialized, dict): # it is a single object ("{}")
            mc = MovementCommand()
            mc.drive = deserialized["drive"]
            mc.steer = deserialized["steer"]
            mc.duration = deserialized["duration"]
            ToReturn.append(mc)
        elif isinstance(deserialized, list): # it is an array of objects ("[]")
            for jobj in deserialized:
                mc = MovementCommand()
                mc.drive = jobj["drive"]
                mc.steer = jobj["steer"]
                mc.duration = jobj["duration"]
                ToReturn.append(mc)
        
        return ToReturn