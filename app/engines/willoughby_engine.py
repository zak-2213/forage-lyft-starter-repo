from engines.engine import Engine

class WilloughbyEngine (Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        if (self.current_mileage - self.last_service_mileage > 60000):
            self.last_service_mileage = self.current_mileage
            return True
        else:
            return False
