# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDeep(node: Optional[TreeNode], currDepth: int) -> int:
            if not node:
                return currDepth - 1
            return max(maxDeep(node.right, currDepth + 1), maxDeep(node.left, currDepth+1))
        return maxDeep(root, 1)