from typing import List

class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:

    def merge(arr, L, M, R):
      left, right = arr[L:M+1], arr[M+1:R+1]

      # i to point nums (in place replace)
      # j to point left array
      # k to point right array
      i, j, k = L, 0, 0
      
      while j < len(left) and k < len(right):
        if left[j] <= right[k]:
          arr[i] = left[j]
          j += 1
        else:
          arr[i] = right[k]
          k += 1
        i += 1

      # add remaining data if either left or right is overbound
      while j < len(left):
        arr[i] = left[j]
        j += 1
        i += 1
      while k < len(right):
        arr[i] = right[k]
        k += 1
        i += 1

    # recursive
    def mergeSort(arr, l, r):

      # exit condition: 
      if l == r:
        return arr
      
      # divide
      m = (l + r) // 2
      mergeSort(arr, l, m)
      mergeSort(arr, m + 1, r)

      # conquer
      merge(arr, l, m, r)

      return arr

    return mergeSort(nums, 0, len(nums) - 1)

if __name__ == "__main__":
  s = Solution()
  nums = [5,1,1,2,0,0]
  print(s.sortArray(nums))