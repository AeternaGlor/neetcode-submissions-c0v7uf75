# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val)])
        res = 0
        while q:
            cur,  c_max = q.pop()
            if cur.val >= c_max:
                res += 1
                c_max = cur.val
            if cur.left:
                q.appendleft((cur.left, c_max))
            if cur.right:
                q.appendleft((cur.right, c_max))
        return res
            



