from typing import List

class MinStack:
  def __init__(self):
    self.stack = []
    self.min_stack = []
    
  def push(self, val: int) -> None:
    self.stack.append(val)
    self.min_stack.append(min(self.min_stack[-1], val) if len(self.min_stack) > 0 else val)

  def pop(self) -> None:
    self.stack.pop()
    self.min_stack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.min_stack[-1]

  

def minStack(operations: List[str], input: List[List[int]]) -> List[int]:
  result = []
  min_stack = MinStack()
  for idx, op in enumerate(operations):
    print(op)
    if op == "push":
      min_stack.push(input[idx][0])
      result.append(None)
    elif op == "pop":
      min_stack.pop()
      result.append(None)
    elif op == "top":
      result.append(min_stack.top())
    elif op == "getMin":
      result.append(min_stack.getMin())
    else:
      result.append(None)

  return result

  

if __name__ == '__main__':
  operations = ["MinStack","push","push","push","getMin","pop","top","getMin"]
  input = [[],[-2],[0],[-3],[],[],[],[]]
  
  print(minStack(operations, input))