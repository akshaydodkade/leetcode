def minCandies(ratings):
  n = len(ratings)
  candies = [1] * n
  
  # traverse left to right
  for i in range(1, n):
      if ratings[i] > ratings[i - 1]:
          candies[i] = candies[i - 1] + 1
  
  # traverse right to left
  for i in range(n - 2, -1, -1):
      if ratings[i] > ratings[i + 1]:
          candies[i] = max(candies[i], candies[i + 1] + 1)

  return sum(candies)

if __name__ == '__main__':
  # i = list(map(int, input().split()))
  ratings = [2, 1, 2]
  print(minCandies(ratings))