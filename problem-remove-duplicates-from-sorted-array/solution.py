def removeDuplicates(nums):
  write = 0

  for num in nums:
    if write < 2 or num > nums[write - 2]:
      nums[write] = num
      write += 1

  del nums[write:]
  return nums


if __name__ == '__main__':
  i = list(map(int, input().split()))
  nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
  print(removeDuplicates(nums))