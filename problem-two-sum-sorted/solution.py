from typing import List 

def twoSum(numbers: List[int], target: int) -> List[int]:
  l, r = 0, len(numbers) - 1
  # approach: two pointers
  while l < r:
      sum = numbers[l] + numbers[r]
      if sum > target:
          # condition: sum is higher need small values
          r = r - 1
      elif sum < target:
          # condition: sum is lesser need high values
          l = l + 1
      else:
          # condition: sum is equal to target
          return [l + 1, r + 1]
  return []
  

if __name__ == '__main__':
  numbers = [2,3,4]
  target = 6
  
  print(twoSum(numbers, target))