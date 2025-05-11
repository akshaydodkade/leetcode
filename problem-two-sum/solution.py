from typing import List

def twoSum(nums: List[int], target: int) -> List:
  # initiate hashmap
  numsMap = {} # value: index


  for i, n in enumerate(nums):
    # check for difference
    diff = target - n

    # search difference in hashmap
    if diff in numsMap:
      return [numsMap[diff], i]
    # if not found then add current value: index in hashmap
    numsMap[n] = i
  return []

if __name__ == '__main__':
  nums = [2, 1, 5, 3]
  target = 4
  
  print(twoSum(nums, target))