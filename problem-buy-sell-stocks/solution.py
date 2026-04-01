from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    l, r = 0, 1 # left = buy, right = sell
    profit = 0
    
    while r < len(prices):
      # check if transaction is profitable
      if prices[l] < prices[r]:
        profit = max(profit, prices[r] - prices[l])
      else:
        l = r
      r += 1
    
    return profit

if __name__ == "__main__":
  s = Solution()
  prices = [7,1,5,3,6,4]
  print(s.maxProfile(prices))