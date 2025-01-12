def validParenthesis(s, locked):
  n = len(s)
  if n % 2 != 0:
    return False
  
  # traverse left to right
  open_slots = 0
  for i in range(n):
    if locked[i] == '0':
      open_slots += 1
    elif s[i] == '(':
      open_slots += 1
    else:
      open_slots -= 1
    
    if open_slots < 0:
      return False
  
  # traverse right to left
  close_slots = 0
  for i in range(n - 1, -1, -1):
    if locked[i] == '0':
      close_slots += 1
    elif s[i] == ')':
      close_slots += 1
    else:
      close_slots -= 1
    
    if close_slots < 0:
      return False
  
  return True

if __name__ == '__main__':
  s = '()'
  locked = [0, 0]
  print(validParenthesis(s, locked))