# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # the algorithm involves adding children to the queue, clearing the queue to create a level
        # appending the values to the result array, adding the children of those into the queue and repeating
        if not root:
            return []
        res = []
        que = deque()
        que.append(root)
        while que:
            level = []
            while que:
                level.append(que.popleft())
            res.append([node.val for node in level])
            for i in level:
                if i.left:
                    que.append(i.left)
                if i.right:
                    que.append(i.right)
        return res
