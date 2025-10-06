from typing import List

class Solution:
  # method: with using division
  def productExceptSelfwithDivision(self, nums: List[int]) -> List[int]:
    res = []

    # get product of entire array
    total = 1
    for i in range(len(nums)):
      total *= nums[i]
    
    # calculate product values
    for j in range(len(nums)):
      res.append(total // nums[j])

    return res

  # method: using separate prefix and postfix
  def productExceptSelfwithPrePost(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    prefix = [1] * n
    postfix = [1] * n
    
    # calculate prefix
    prefix[0] = 1
    for i in range(1, n):
      prefix[i] = prefix[i - 1] * nums[i - 1]

    # calculate postfix
    postfix[-1] = 1
    for j in range(n - 2, -1, -1):
      postfix[j] = postfix[j + 1] * nums[j + 1]

    # calculate res
    for k in range(n):
      res[k] = prefix[k] * postfix[k]
    return res

  def productExceptSelf(self, nums: List[int]) -> List[int]:
    # without using seperate prefix and postfix
    n = len(nums)
    res = [1] * n

    # calculate prefix and store it in res
    prefix = 1
    for i in range(n):
      res[i] = prefix
      prefix *= nums[i]

    # calculate postfix and store it in res
    postfix = 1
    for i in range(n - 1, -1, -1):
      res[i] *= postfix
      postfix *= nums[i]

    return res

if __name__ == "__main__":
  nums = [-1,0,1,2,3]

  s = Solution()
  print(s.productExceptSelf(nums))