import array
from tires.tire import Tire

class OctoprimeTires (Tire):
    def __init__(self, tire_wear: array):
        self.tire_wear = tire_wear
    
    def needs_service(self) -> bool:
        sum = 0
        
        for i in self.tire_wear:
            sum = sum + i
        
        return sum >= 3
