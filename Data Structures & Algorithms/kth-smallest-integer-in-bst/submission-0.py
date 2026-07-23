# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(curr: Optional[TreeNode]) -> None:
            nonlocal res
            nonlocal k
            if not curr:
                return
            inorder(curr.left)
            if len(res) == k:
                return
            res.append(curr.val)
            inorder(curr.right)
        inorder(root)
        return res[-1]
            