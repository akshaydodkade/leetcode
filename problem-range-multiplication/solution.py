class Solution:
  def xorAfterQueries(self, nums, queries):
    MOD = 10**9 + 7
    
    for l, r, k, v in queries:
        for i in range(l, r + 1, k):
            nums[i] = (nums[i] * v) % MOD
    
    result = 0
    for num in nums:
        result ^= num
    
    return result


if __name__ == '__main__':
  s = Solution()
  nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]
  print(s.xorAfterQueries(nums, queries))