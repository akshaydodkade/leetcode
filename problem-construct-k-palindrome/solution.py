from collections import Counter

def constructPalindrome(s, k):
  char_count = Counter(s)
  odd_count = sum(1 for count in char_count.values() if count %2 != 0)
  return odd_count <= k <= len(s)


if __name__ == '__main__':
  i = list(map(int, input().split()))
  s = 'annabelle'
  k = 2
  print(constructPalindrome(s, k))