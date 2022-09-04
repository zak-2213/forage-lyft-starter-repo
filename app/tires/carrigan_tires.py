from array import array
from tires.tire import Tire

class CarriganTires (Tire):
    def __init__(self, tire_wear: array):
        self.tire_wear = tire_wear
    
    def needs_service(self) -> bool:
        val = False
        
        for i in self.tire_wear:
            if i >= 0.9:
                val = True
        
        return val
