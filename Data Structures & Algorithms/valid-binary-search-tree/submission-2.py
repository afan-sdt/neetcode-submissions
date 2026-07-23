# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def isValid(node: Optional[TreeNode], left: int, right: int):
            if not node:
                return True
            if not (left<node.val<right):
                return False
            return isValid(node.right, node.val, right) and isValid(node.left, left, node.val)
        
        return isValid(root, -100000000, 10000000)