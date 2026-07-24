# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # compare root to root of subroot, if equal, check if tree is same
        #if not same, see if the left or right subtree are the same

        def isSameTree(p, q) -> bool:
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not subRoot: 
            return True
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root and subRoot and root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        