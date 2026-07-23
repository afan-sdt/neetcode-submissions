# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #you can calculate the diameter of a binary tree by calculating the 
        # diameter of the left tree and the right tree and adding one (this node)
        res = 0

        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res