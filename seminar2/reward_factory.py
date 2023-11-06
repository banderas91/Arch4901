from discount_reward import DiscountReward
from gift_reward import GiftReward  
from cashback_reward import CashbackReward
from premium_status_reward import PremiumStatusReward
from lottery_reward import LotteryReward

class RewardFactory:

  @staticmethod
  def create_discount():
    return DiscountReward()

  @staticmethod
  def create_gift():
    return GiftReward()

  @staticmethod
  def create_cashback():
    return CashbackReward()

  @staticmethod
  def create_premium_status():
    return PremiumStatusReward()

  @staticmethod
  def create_lottery():
    return LotteryReward()

  
 
