class Solution:
  def template(self, n):
    return n


if __name__ == '__main__':
  n = list(map(int, input().split()))
  s = Solution()
  print(s.template(n))