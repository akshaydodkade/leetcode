from typing import List
import collections

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def levelOrder(self, root=TreeNode) -> List[List[int]]:
    res = []

    # convert root to deque (double ended queue)
    q = collections.deque()
    q.append(root)
    
    while q:
      q_len = len(q)
      level = []

      for i in range(q_len):
        node = q.popleft()
        if node:
          level.append(node.val)
          q.append(node.left)
          q.append(node.right)

      if level:
        res.append(level)

    return res

def buildTree(arr):
  if not arr:
    return None
  
  root = TreeNode(arr[0])
  q = collections.deque([root])
  i = 1
  while i < len(arr):
    node = q.popleft()

    if i < len(arr):
      node.left = TreeNode(arr[i])
      q.append(node.left)
      i += 1
  
    if i < len(arr):
      node.right = TreeNode(arr[i])
      q.append(node.right)
      i += 1

  return root

if __name__ == "__main__":
  root = [1,2,3,4,5,6,7]
  s = Solution()
  print(s.levelOrder(buildTree(root)))