# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root:
            return False

        def isEqual(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            elif not p:
                return False
            elif not q:
                return False
            if p.val != q.val:
                return False
            return isEqual(p.left, q.left) and isEqual(p.right, q.right)

        if isEqual(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        