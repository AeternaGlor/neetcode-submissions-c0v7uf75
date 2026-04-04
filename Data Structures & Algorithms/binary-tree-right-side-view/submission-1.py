# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []

        if not root:
            return res
        while q:
            curr_lvl = []
            for i in range(len(q)):
                cur = q.pop()
                curr_lvl.append(cur.val)
                if cur.left:
                    q.appendleft(cur.left)
                if cur.right:
                    q.appendleft(cur.right)
            res.append(curr_lvl[-1])
        return res
