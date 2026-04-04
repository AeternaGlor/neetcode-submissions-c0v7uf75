# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur_min =  -2 * 10**31 - 1
        cur_max =  2 * 10**31

        q = collections.deque([(root, cur_min, cur_max)])

        while q:
            for i in range(len(q)):
                curr, cur_min, cur_max = q.pop()

                if cur_min >= curr.val or curr.val >= cur_max:
                    return False

                if curr.left:
                    q.appendleft((curr.left, cur_min, curr.val))
                if curr.right:
                    q.appendleft((curr.right, curr.val, cur_max))

        return True