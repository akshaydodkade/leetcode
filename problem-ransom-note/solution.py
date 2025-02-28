from collections import Counter

def checkMagazine(magazine, ransomNote):
  magazineCount = Counter(magazine)
  ransomCount = Counter(ransomNote)

  for char, count in ransomCount.items():
    if magazineCount[char] < count:
      return False
  return True

if __name__ == '__main__':
  magazine = 'aa'
  ransomNote = 'ab'
  print(checkMagazine(magazine, ransomNote))