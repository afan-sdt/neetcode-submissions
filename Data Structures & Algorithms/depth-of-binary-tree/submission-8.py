# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        que = deque()
        res = 0
        if root:
            que.append(root)
        while que:
            size = len(que)
            for i in range(size):
                curr = que.popleft()
                if curr.right:
                    que.append(curr.right)
                if curr.left:
                    que.append(curr.left)
            res += 1
        return res