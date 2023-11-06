from rewards import Reward

class PremiumStatusReward(Reward):

  def use(self):
    print("Получен премиум статус")
