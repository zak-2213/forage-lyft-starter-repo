from datetime import date
from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from car import Car
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine


class CarFactory ():
    def create_calliope (current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def create_glissade (current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def create_palindrome (current_date: date, last_service_date: date, warning_light_on: bool):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))
    
    def create_rorschach (current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))

    def create_thovex (current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))
