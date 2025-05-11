

def isAnagram(s: str, t: str) -> bool:
  # s & t length should be equal
  if len(s) != len(t):
    return False
  
  sHash, tHash = {}, {} # char: count

  # create hash map for for s and t
  for i in range(len(s)):
    sHash[s[i]] = 1 + sHash.get(s[i], 0)
    tHash[t[i]] = 1 + tHash.get(t[i], 0)
  
  # check if hash map have equal counts
  for c in sHash:
    if sHash[c] != tHash.get(c, 0):
      return False

  return True

if __name__ == '__main__':
  # s = "anagram"
  # t = "nagaram"
  s = "rat"
  t = "car"
  
  print(isAnagram(s, t))