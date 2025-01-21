def validStackParenthesis(s):
  stack = []
  current_result = 0
  num = 0
  sign = 1  # 1 for '+', -1 for '-'

  for char in s:
    if char.isdigit():
      num = num * 10 + int(char)  # Build the number
    elif char == '+':
      current_result += sign * num
      num = 0
      sign = 1
    elif char == '-':
      current_result += sign * num
      num = 0
      sign = -1
    elif char == '(':
      # Push current state onto the stack
      stack.append(current_result)
      stack.append(sign)
      # Reset for the new level
      current_result = 0
      sign = 1
    elif char == ')':
      # Complete the current level calculation
      current_result += sign * num
      num = 0
      # Pop the sign and previous result
      current_result *= stack.pop()  # Multiply by the sign
      current_result += stack.pop()  # Add the previous result
    
    print(char, num, current_result)
    print(stack)
  
  current_result += sign * num
  return current_result

if __name__ == '__main__':
  s = '(1+(4+5+2)-3)+(6+8)'
  print(validStackParenthesis(s))