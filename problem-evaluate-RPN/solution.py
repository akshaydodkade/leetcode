from typing import List

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack = []

    for t in tokens:
      if t == "+":
        stack.append(stack.pop() + stack.pop())
      elif t == "-":
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)
      elif t == "*":
        stack.append(stack.pop() * stack.pop())
      elif t == "/":
        b, a = stack.pop(), stack.pop()
        stack.append(int(a / b))
      else:
        stack.append(int(t))

    return stack[-1]

if __name__ == "__main__":
  s = Solution()
  # tokens = ["2","1","+","3","*"]
  # tokens = ["4","13","5","/","+"]
  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
  print(s.evalRPN(tokens))