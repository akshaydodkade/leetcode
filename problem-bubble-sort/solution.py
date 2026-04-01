from typing import List

class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)):
      swapped = False
      for j in range(len(nums) - (i + 1)):
        if nums[j] > nums[j+1]:
          nums[j], nums[j+1] = nums[j+1], nums[j]
          swapped = True
      if not swapped:
        return nums

    return nums

if __name__ == '__main__':
  s = Solution()
  # nums = [5,1,1,2,0,0]
  # nums = [5,2,3,1]
  nums = [1,2,5,4]
  print(s.sortArray(nums))