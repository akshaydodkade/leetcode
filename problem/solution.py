from collections import defaultdict, Counter

class Solution:
  def minimumHammingDistance(self, source, target, allowedSwaps):
    n = len(source)
    # DSU
    parent = list(range(n))
    
    def find(x):
      if parent[x] != x:
        parent[x] = find(parent[x])
      return parent[x]
    
    def union(x, y):
      px, py = find(x), find(y)
      if px != py:
        parent[py] = px
    
    # Step 1: Build components
    for a, b in allowedSwaps:
      union(a, b)
    
    # Step 2: Group indices
    groups = defaultdict(list)
    for i in range(n):
      groups[find(i)].append(i)
    
    # Step 3: Count mismatches
    hamming = 0
    
    for indices in groups.values():
      freq = Counter()
      
      # count source values
      for i in indices:
        freq[source[i]] += 1
      
      # match target values
      for i in indices:
        if freq[target[i]] > 0:
          freq[target[i]] -= 1
        else:
          hamming += 1
    
    return hamming


if __name__ == '__main__':
  s = Solution()
  source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
  print(s.minimumHammingDistance(source, target, allowedSwaps))