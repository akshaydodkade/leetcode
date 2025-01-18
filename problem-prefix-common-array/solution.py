def prefixCommon(A, B):
  n = len(A)
  seenA, seenB = set(), set()
  commonCount = 0
  C = []
  
  for i in range(n):
    if A[i] in seenB:
      commonCount += 1
    if B[i] in seenA:
      commonCount += 1
    
    seenA.add(A[i])
    seenB.add(B[i])
    
    if A[i] == B[i]:
      commonCount -= 1
    
    C.append(commonCount)
  
  return C

if __name__ == '__main__':
  # i = list(map(int, input().split()))
  A = [2,3,1]
  B = [3,1,2]
  prefixCommon(A, B)
  # print(validSudoku(board))