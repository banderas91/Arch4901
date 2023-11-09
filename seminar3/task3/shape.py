from abc import ABC, abstractmethod

class Shape2D(ABC):
    @abstractmethod
    def area(self):
        pass
