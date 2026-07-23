# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nextLevel=[]
        nextLevel.append(root)
        res = []
        while nextLevel:
            temp = nextLevel
            res.append([node.val for node in temp])
            nextLevel = []
            for node in temp:
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)
        return res

            