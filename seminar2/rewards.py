from abc import ABC, abstractmethod

class Reward(ABC):

  @abstractmethod
  def use(self):
    pass

