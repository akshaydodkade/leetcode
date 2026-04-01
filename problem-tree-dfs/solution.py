from typing import List, Optional
import collections


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# DFS Traversals
class Solution:
  def preorder(self, root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
      if not node:
        return
      result.append(node.val)    # Root
      dfs(node.left)             # Left
      dfs(node.right)            # Right

    dfs(root)
    return result

  def inorder(self, root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
      if not node:
        return
      dfs(node.left)             # Left
      result.append(node.val)    # Root
      dfs(node.right)            # Right

    dfs(root)
    return result

  def postorder(self, root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
      if not node:
        return
      dfs(node.left)             # Left
      dfs(node.right)            # Right
      result.append(node.val)    # Root

    dfs(root)
    return result


# Helper: Convert list → Binary Tree
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


# Example usage:
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5, 6, 7]
  tree = buildTree(arr)

  s = Solution()
  print("Preorder :", s.preorder(tree))
  print("Inorder  :", s.inorder(tree))
  print("Postorder:", s.postorder(tree))
