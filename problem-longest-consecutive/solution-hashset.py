from typing import List
from collections import defaultdict

def longestConsecutive(nums: List[int]) -> int:
  numsSet = set(nums)
  longest = 0

  for num in numsSet:
    long = 0
    # check if num is start of sequence (-1)
    if num - 1 in numsSet:
      # if not initial then skip
      continue
    else:
      # if initial store in numsCount and check for other consecutives
      value = num + 1
      long = 1
      while value in numsSet:
        long += 1
        value += 1
    
      longest = max(long, longest)

  return longest

if __name__ == '__main__':
  nums = [100, 4, 200, 1, 3, 2]
  print(longestConsecutive(nums))