# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        depths = {None: 0}
        while stack:
            curr = stack.pop()
            if not curr: 
                continue
            if curr not in depths:
                depths[curr] = 0
                stack.append(curr)
                stack.append(curr.right)
                stack.append(curr.left)
            else:
                if abs(depths[curr.left] - depths[curr.right]) > 1:
                    return False
                depths[curr] = 1 + max(depths[curr.left], depths[curr.right])
        
        return True
