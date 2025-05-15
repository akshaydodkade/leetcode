from typing import List

def containsDuplicate(nums: List[int]) -> bool:
  numsHashset = set([])
  for num in nums:
    if num in numsHashset:
      return True
    else:
      numsHashset.add(num)
    
  return False

if __name__ == '__main__':
  nums = [1, 2, 3, 1]
  # nums = [1,5,-2,-4,0]
  print(containsDuplicate(nums))