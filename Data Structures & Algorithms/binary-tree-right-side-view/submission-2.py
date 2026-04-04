class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(root, depth, res):
            if not root:
                return
            if len(res) == depth:
                res.append(root.val)
            dfs(root.right, depth + 1, res)
            dfs(root.left, depth + 1, res)
            return

        dfs(root, 0, res)
        return res