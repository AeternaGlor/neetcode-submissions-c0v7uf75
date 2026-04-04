# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_same(self, root1, root2):
        if not root1 and not  root2:
            return True
        if not root1 or not  root2 or root1.val != root2.val:
            return False

        l = self.is_same(root1.left, root2.left)
        r = self.is_same(root1.right, root2.right)
        return l and r
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.is_same(root, subRoot):
            return True
        
        r = l = False

        if root.left:
            l = self.isSubtree(root.left, subRoot)
        if root.right:
            r = self.isSubtree(root.right, subRoot)

        # if r or l:
        #     return True    
        return r or l    