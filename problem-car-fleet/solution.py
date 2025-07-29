from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
  pair = [[p, s] for p, s in zip(position, speed)] # format [[p, s]]

  # loop in reversed sorted order of pair
  stack = []
  for p, s in sorted(pair)[::-1]:
    stack.append((target - p) / s) # get the time(t) to reach target
    if len(stack) >= 2 and stack[-1] <= stack[-2]:
      stack.pop()
  
  return len(stack)

if __name__ == '__main__':
  target = 100
  position = [0, 2, 4]
  speed = [4, 2, 1]
  
  print(carFleet(target, position, speed))