from typing import List

def twoSum(nums: List[int], target: int) -> List:
  # forward loop to check the sums
  for i in range(len(nums)):
    for j in range((i + 1), len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
      
  # return empty list for no sum matching target
  return []

if __name__ == '__main__':
  nums = [2, 1, 5, 3]
  target = 4
  
  print(twoSum(nums, target))