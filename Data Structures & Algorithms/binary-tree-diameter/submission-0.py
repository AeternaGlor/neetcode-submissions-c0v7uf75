# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def DFS(root):
            if not root:
                return 0, 0

            d_left, longest_path_left = DFS(root.left)
            d_right, longest_path_right = DFS(root.right)

            longest_path = 1 + max(longest_path_left, longest_path_right)
            d_max = max(d_left, d_right, 
                        longest_path_left + longest_path_right)

            return d_max, longest_path
        
        d_max, _ = DFS(root)
        return d_max