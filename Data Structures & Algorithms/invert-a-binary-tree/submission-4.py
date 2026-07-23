# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deq = deque()
        deq.append(root)
        while deq:
            curr = deq.pop()
            if not curr:
                continue
            curr.right, curr.left = curr.left, curr.right
            deq.append(curr.right)
            deq.append(curr.left)
        return root