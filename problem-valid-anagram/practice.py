def isValidAnagram(s: str, t: str) -> bool:
  # base case
  if len(s) != len(t):
    return False
  
  sHash, tHash = {}, {} # { char: count }

  # add count values in hash
  for i in range(len(s)):
    sHash[s[i]] = 1 + sHash.get(s[i], 0)
    tHash[t[i]] = 1 + tHash.get(t[i], 0)
  
  # check for character count
  for c in sHash:
    if sHash[c] != tHash.get(c, 0):
      return False

  return True


if __name__ == "__main__":
  s = "cat"
  t = "tac"
  print(isValidAnagram(s, t))