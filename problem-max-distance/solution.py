from typing import List

class Solution:
  def maxDistance(self, colors: List[int]) -> int:
    n = len(colors)
    
    ans = 0
    
    # Compare with first element
    for j in range(n - 1, -1, -1):
      if colors[j] != colors[0]:
        ans = max(ans, j)
        break
    
    # Compare with last element
    for i in range(n):
      if colors[i] != colors[n - 1]:
        ans = max(ans, n - 1 - i)
        break
    
    return ans


if __name__ == '__main__':
  s = Solution()
  colors = [1,8,3,8,3]
  print(s.maxDistance(colors))