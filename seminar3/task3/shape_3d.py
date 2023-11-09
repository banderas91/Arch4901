from abc import ABC, abstractmethod

class Shape3D(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass
