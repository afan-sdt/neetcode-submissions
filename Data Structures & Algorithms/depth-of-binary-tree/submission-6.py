# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        deq = deque([(root,1)])
        while deq:
            curr = deq.pop()
            if not curr[0]:
                continue
            res = max(res, curr[1])
            deq.append((curr[0].left, curr[1] + 1))
            deq.append((curr[0].right, curr[1] + 1))
        return res