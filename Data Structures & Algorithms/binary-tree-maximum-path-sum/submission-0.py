class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        abs_max = float("-inf")

        def DFS(root):
            nonlocal abs_max
            l = r = 0
            curr_max = root.val
            
            if root.left:
                l = DFS(root.left)
                l = max(l, 0)
            if root.right:
                r = DFS(root.right)
                r = max(r, 0)
            
            # если макс тропа проходит через текущий корень
            tmp = curr_max + l + r 
            # т.к через одну вершину можем пройти лишь единожды
            curr_max += max(l, r) 

            abs_max = max(abs_max, tmp)
            return curr_max
        
        DFS(root)
        return abs_max