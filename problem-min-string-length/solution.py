def minString(s):
  charFrequency = [0] * 26
  totalLength = 0

  for char in s:
    charFrequency[ord(char) - ord('a')] += 1

  for freq in charFrequency:
    if freq == 0:
        continue
    if freq % 2 == 0:
        totalLength += 2
    else:
        totalLength += 1

  return totalLength

if __name__ == '__main__':
  s = 'aa'
  print(minString(s))