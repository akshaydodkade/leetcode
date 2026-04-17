from math import isqrt
from collections import defaultdict

class Solution:
  def minAbsoluteDistance(self, nums):
    def reverse_num(x):
        return int(str(x)[::-1])
    
    last_seen = {}
    ans = float('inf')
    
    for j, num in enumerate(nums):
        # check if current number matches any previous reversed
        if num in last_seen:
            ans = min(ans, j - last_seen[num])
        
        # store reverse of current number
        rev = reverse_num(num)
        last_seen[rev] = j
    
    return ans if ans != float('inf') else -1


if __name__ == '__main__':
  s = Solution()
  nums = [12,21,45,33,54]
  print(s.minAbsoluteDistance(nums))