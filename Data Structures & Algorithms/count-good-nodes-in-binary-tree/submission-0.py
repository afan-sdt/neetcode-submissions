# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node: TreeNode, maxSoFar: int):
            nonlocal count
            if not node:
                return None
            
            if node.val >= maxSoFar:
                count += 1
                maxSoFar = node.val
            
            dfs(node.right, maxSoFar)
            dfs(node.left, maxSoFar)
        
        dfs(root, -150)
        return count