# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        def DFS(node, start_min):
            curr_min = 1 + start_min

            if node.left:
                curr_min += DFS(node.left, start_min) - start_min
            
            if curr_min == k:
                nonlocal res
                res = node.val
                print(node.val)
                # return 

            if node.right:
                curr_min = DFS(node.right, curr_min)
            
            return curr_min
        
        DFS(root, 0)
        return res    