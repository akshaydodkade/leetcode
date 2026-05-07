from typing import List

class Solution:
  def maxReachable(self, nums: List[int]) -> List[int]:
    n = len(nums)

    # suffix minimum
    suf_min = [0] * n
    suf_min[-1] = nums[-1]

    for i in range(n - 2, -1, -1):
      suf_min[i] = min(nums[i], suf_min[i + 1])

    ans = [0] * n

    start = 0
    pref_max = nums[0]

    for i in range(n):
      pref_max = max(pref_max, nums[i])

      # component boundary
      if i == n - 1 or pref_max <= suf_min[i + 1]:
        comp_max = max(nums[start:i + 1])

        for j in range(start, i + 1):
          ans[j] = comp_max

        start = i + 1

        if start < n:
          pref_max = nums[start]

    return ans


if __name__ == '__main__':
  s = Solution()
  nums = [2,1,3]
  print(s.maxReachable(nums))