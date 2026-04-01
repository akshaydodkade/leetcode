from typing import Optional
import collections

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# build tree
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

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
  s = Solution()
  root = [3,9,20,None,None,15,7]

  print(s.maxDepth(buildTree(root)))
