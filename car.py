from battery.battery import Battery
from engine.engine import Engine
from servicable import Servicable

class Car (Servicable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
