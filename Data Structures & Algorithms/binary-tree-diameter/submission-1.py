# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(node:TreeNode) -> int:
            nonlocal res
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            res = max(res, l+r)
            return 1 + max(l, r)
        depth(root)
        return res
