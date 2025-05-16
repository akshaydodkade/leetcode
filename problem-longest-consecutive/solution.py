from typing import List
from collections import defaultdict

def longestConsecutive(nums: List[int]) -> int:
  numsSet = set(nums)
  longest = 0

  for num in numsSet:
    # check if num is start of sequence (-1)
    if num - 1 not in numsSet:
    # if initial store in numsCount and check for other consecutives
      long = 1 # make current num as long
      while (num + long) in numsSet:
        long += 1
      longest = max(long, longest)
  return longest

if __name__ == '__main__':
  nums = [100, 4, 200, 1, 3, 2]
  print(longestConsecutive(nums))