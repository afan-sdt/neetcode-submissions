# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def bottomUp(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(bottomUp(node.left) + 1, bottomUp(node.right) + 1)
        return bottomUp(root)