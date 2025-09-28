from typing import List
import math

def minEatingSpeed(piles: List[int], h: int) -> int:
  l, r = 1, max(piles)
  res = r
  
  while l <= r:
    k = (l + r) // 2
    hours = 0
    for p in piles:
      hours += math.ceil(p / k)
    
    if hours <= h:
      res = min(res, k)
      r = k - 1
    else:
      l = k + 1
  
  return res



if __name__ == "__main__":
  piles = [312884470]
  h = 968709470
  print(minEatingSpeed(piles, h))