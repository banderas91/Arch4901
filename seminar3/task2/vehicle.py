from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed

    @abstractmethod
    def calculate_allowed_speed(self):
        pass
