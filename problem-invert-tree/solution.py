from typing import Optional
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  # recursive method
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # exit condition
    if not root:
      return None
    
    # swap childern
    tmp = root.left
    root.left = root.right
    root.right = tmp

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root
  
# utility: list to tree
def list_to_tree(lst):
  if not lst:
    return None
  
  root = TreeNode(lst[0])
  queue = deque([root])
  i = 1
  while queue and i < len(lst):
    node = queue.popleft()
    if i < len(lst) and lst[i] is not None:
      node.left = TreeNode(lst[i])
      queue.append(node.left)
    i += 1
    if i < len(lst) and lst[i] is not None:
      node.right = TreeNode(lst[i])
      queue.append(node.right)
    i += 1
  return root

# utility: tree to list
def tree_to_list(root):
  if not root:
    return []
  res = []
  queue = deque([root])
  while queue:
    node = queue.popleft()
    if node:
      res.append(node.val)
      queue.append(node.left)
      queue.append(node.right)
    else:
      res.append(None)

  while res and res[-1] is None:
    res.pop()
  return res


if __name__ == "__main__":
  s = Solution()
  root = [4, 2, 7, 1, 3, 6, 9]
  print(tree_to_list(s.invertTree(list_to_tree(root))))