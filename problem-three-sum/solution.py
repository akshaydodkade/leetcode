from typing import List

class Solution:
  # method: two pointers
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []

    # sort nums array
    nums.sort()
    
    for i, a in enumerate(nums):
      # base case
      if a > 0:
        break

      # skip duplicate values
      if i > 0 and a == nums[i - 1]:
        continue

      # use 2 pointers for remaining data
      l, r = i + 1, len(nums) - 1
      while l < r:
        sum = a + nums[l] + nums[r]
        if sum > 0:
          # sum is higher - decrease right
          r -= 1
        elif sum < 0:
          # sum is lower - increase left
          l += 1
        else:
          # sum is 0 so store the values
          res.append([a, nums[l], nums[r]])
          l += 1
          r -= 1
          # skip duplicate res (eg: [-2, -2, 0, 0, 2, 2])
          while nums[l] == nums[l - 1] and l < r:
            l += 1

    return res
  
if __name__ == "__main__":
  s = Solution()
  nums = [-1, 0, 1, 2, -1, -4]
  # nums = [-2, -2, 0, 0, 2, 2]
  print(s.threeSum(nums))