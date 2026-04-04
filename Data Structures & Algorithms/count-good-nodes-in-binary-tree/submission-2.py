# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        res = 0
        while stack:
            cur, c_max = stack.pop()
            if cur.val >= c_max:
                c_max = cur.val
                res += 1
            if cur.right:
                stack.append((cur.right, c_max))
            if cur.left:
                stack.append((cur.left, c_max))
        return res
        
        


            



