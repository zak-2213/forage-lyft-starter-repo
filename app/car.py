from batteries.battery import Battery
from engines.engine import Engine
from tires.tire import Tire
from servicable import Servicable

class Car (Servicable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
