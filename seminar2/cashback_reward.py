from rewards import Reward

class CashbackReward(Reward):

  def use(self):
    print("Начислен кешбек")
