import heapq

def second_largest(arr):
  heap = [-x for x in arr]
  heapq.heapify(heap)

  largest = -heapq.heappop(heap)
  while heap:
    second = -heapq.heappop(heap)
    if second != largest:
      return second

if __name__ == "__main__":
  print(second_largest([4, 6, 8, 9, 10]))