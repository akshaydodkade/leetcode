def isAnagram(s: str, t: str) -> bool:

  # base case
  if len(s) != len(t): return False # length should be equal
  
  sList = list(s)
  tList = list(t)

  for char in sList:
    if char in tList:
      tList.remove(char)
    else:
      return False

  if len(tList):
    return False
  
  return True

if __name__ == '__main__':
  s = "anagram"
  t = "nagaram"
  # s = "rat"
  # t = "car"
  
  print(isAnagram(s, t))