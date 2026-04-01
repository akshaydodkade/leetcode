class Solution:
  def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
    n = len(positions)

    # Step 1: combine and sort
    robots = []
    for i in range(n):
      robots.append((positions[i], healths[i], directions[i], i))

    robots.sort()  # sort by position

    stack = []  # will store indices of robots (in robots array)

    # Convert to mutable list
    health = [h for _, h, _, _ in robots]

    for i in range(n):
      pos, h, d, idx = robots[i]
      
      if d == 'R':
        stack.append(i)
      else:
        # moving left
        while stack and health[i] > 0:
          j = stack[-1]  # last R robot
          
          if health[j] < health[i]:
            # R dies
            stack.pop()
            health[i] -= 1
            health[j] = 0
          
          elif health[j] > health[i]:
            # L dies
            health[j] -= 1
            health[i] = 0
            break
          
          else:
            # both die
            stack.pop()
            health[j] = 0
            health[i] = 0
            break

    # Step 4: collect survivors
    result = []
    for i in range(n):
      if health[i] > 0:
        result.append((robots[i][3], health[i]))  # (original index fhealth)

    # sort by original index
    result.sort()

    return [h for _, h in result]


if __name__ == '__main__':
  s = Solution()
  positions = [5,4,3,2,1]
  healths = [2,17,9,15,10]
  directions = "RRRRR"
  print(s.survivedRobotsHealths(positions, healths, directions))