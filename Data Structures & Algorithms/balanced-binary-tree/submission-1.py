# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #calculate height of left and right and return if they're balanced
        # to calculate height: base case if no node, return 0
        #height of current node is max of height of left or height of right
        # we can keep a global balanced variable that represents if the invariant is broken

        res = True

        def height(node) -> int:
            if not node:
                return 0
            nonlocal res
            heightLeft = height(node.left)
            heightRight = height(node.right)
            if abs( heightLeft - heightRight ) > 1:
                res = False
            return 1 + max(heightLeft, heightRight)
        height(root)
        return res
        