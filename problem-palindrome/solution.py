def isPalindrome(s):
  filteredString = ''.join(char.lower() for char in s if char.isalnum())
  stringArray = list(filteredString)

  reverseStringArray = stringArray[::-1]

  return stringArray == reverseStringArray

if __name__ == '__main__':
  s = "A man, a plan, a canal: Panama11"
  print(isPalindrome(s))