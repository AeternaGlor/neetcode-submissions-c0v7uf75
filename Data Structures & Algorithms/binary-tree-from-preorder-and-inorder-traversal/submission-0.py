# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indxs = {}
        for i, v in enumerate(inorder):
            indxs[v] = i
        
        def build(l, r, offset):
            if l > r:
                return None

            root = TreeNode(preorder[l])

            mid = indxs[root.val] - offset

            root.left = build(l+1, l+mid, offset)
            root.right = build(l+mid+1, r, offset + mid + 1)

            return root
        
        return build(0, len(preorder)-1, 0)