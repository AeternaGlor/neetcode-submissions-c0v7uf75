# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        visited = {None: (0, 0)}

        while stack:
            curr = stack.pop()
            if not curr:
                continue            

            if not curr in visited:
                stack.append(curr)
                visited[curr] = (0, 0)
                stack.append(curr.right)
                stack.append(curr.left)
            else:
                d_left, longest_path_left = visited[curr.left]
                d_right, longest_path_right = visited[curr.right]

                longest_path = 1 + max(longest_path_left, longest_path_right)
                d_max = max(d_left, d_right, 
                            longest_path_left + longest_path_right)
                
                visited[curr] = (d_max, longest_path)
        
        return visited[root][0]
