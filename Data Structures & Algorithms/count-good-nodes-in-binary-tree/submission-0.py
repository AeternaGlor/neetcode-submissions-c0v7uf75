# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, c_max):
            if not root:
                return
            if root.val >= c_max:
                c_max = root.val
                nonlocal res
                res += 1
            dfs(root.left, c_max)
            dfs(root.right, c_max)
        dfs(root, root.val)
        return res

