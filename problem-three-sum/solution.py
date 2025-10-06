from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
  res = [1] * (len(nums))

  # do prefix calculations
  prefix = 1
  for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]
  
  # do postfix calculations
  postfix = 1
  for i in range(len(nums) - 1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]

  return res


if __name__ == '__main__':
  nums = [1, 2, 4, 6]
  print(productExceptSelf(nums))