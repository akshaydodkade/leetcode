def mergeArrays(num1, num2, m, n):
  p1, p2, p = m - 1, n - 1, m + n - 1

  while p1 >= 0 and p2 >= 0:
    if num2[p2] > num1[p1]:
      num1[p] = num2[p2]
      p2 -= 1
    else:
      num1[p] = num1[p1]
      p1 -= 1
    p -= 1

  # sorting p2
  while p2 >= 0:
    num1[p] = num2[p2]
    p2 -= 1
    p -= 1
  
  return num1


if __name__ == '__main__':
  i = list(map(int, input().split()))
  num1 = [1, 4, 5, 0, 0, 0, 0, 0]
  num2 = [2, 3, 4, 4, 8]
  print(mergeArrays(num1, num2, 3, 5))