class Solution:
  def template(self, positions, healths, direction):
    print(positions, healths, direction)
    return 'end'


if __name__ == '__main__':
  s = Solution()
  positions = [5,4,3,2,1]
  healths = [2,17,9,15,10]
  directions = "RRRRR"
  print(s.template(positions, healths, directions))