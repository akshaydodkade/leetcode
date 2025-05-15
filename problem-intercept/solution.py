from typing import List

def intercept(*a: List[List[int]]) -> List[int]:
  aHashlist = set([])
  resHashlist = set([])

  # traverse all list of a
  for row in a:
    rowHashset = set(row)
    for num in rowHashset:
      if num in aHashlist:
        resHashlist.add(num)
      else:
        aHashlist.add(num)
  
  return list(resHashlist)

if __name__ == '__main__':
  print(intercept(
    [1, 5, 9, 9], 
    [1, 3, 5], 
    [1, 5, 8],
    [100, 150, 300, 500, 1, 5],
  ))