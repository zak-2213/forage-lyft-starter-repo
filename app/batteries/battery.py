from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from servicable import Servicable

class Battery (Servicable):
    def needs_service():
        pass