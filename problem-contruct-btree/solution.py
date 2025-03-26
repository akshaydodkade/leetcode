from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> 'TreeNode':
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    
    def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> 'TreeNode':
        if pre_start > pre_end:
            return None
            
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        
        root_idx = inorder_map[root_val]
        
        left_size = root_idx - in_start
        
        root.left = build(pre_start + 1, 
                        pre_start + left_size,
                        in_start, 
                        root_idx - 1)
        root.right = build(pre_start + left_size + 1,
                          pre_end,
                          root_idx + 1,
                          in_end)
        
        return root
    
    return build(0, len(preorder) - 1, 0, len(inorder) - 1)
  
def printTree(root: TreeNode) -> None:
  if not root:
    print("Empty tree")
    return
  
  queue = [root]
  result = []
  
  while queue:
    level_size = len(queue)
    current_level = []
    
    for _ in range(level_size):
      node = queue.pop(0)
      if node:
        current_level.append(node.val)
        queue.append(node.left if node.left else None)
        queue.append(node.right if node.right else None)
      else:
        current_level.append(None)
    
    if any(val is not None for val in current_level):
      result.extend(current_level)
  
  print(result)


if __name__ == '__main__':
  preorder = [3,9,20,15,7]
  inorder = [9,3,15,20,7]
  solution = Solution()
  tree = solution.buildTree(preorder, inorder)
  printTree(tree)