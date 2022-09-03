from datetime import date, datetime
from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from batteries.battery import Battery

class NubbinBattery (Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service (self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            self.last_service_date = self.current_date
            return True
        else:
            return False