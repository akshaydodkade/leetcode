from typing import List

class Solution:
  def binarySearch(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
      # find mid value
      # m = (l + r) // 2
      m = l + ((r - l) // 2) # optimitsed for out of bound exception
      if nums[m] < target:
        l = m + 1
      elif nums[m] > target:
        r = m - 1
      else:
        return m

    return -1


if __name__ == "__main__":
  nums = [-1,0,3,5,9,12]
  target = 9

  s = Solution()
  print(s.binarySearch(nums, target))