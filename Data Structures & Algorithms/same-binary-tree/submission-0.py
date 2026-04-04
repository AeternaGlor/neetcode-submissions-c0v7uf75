# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        elif not q or not p:
            return False
        
        p1 = deque([p])
        q1 = deque([q])

        while p1 and q1:
            # if len(q1) != len(p1):
            #     return False
            for _ in range(len(p1)):
                q_cur = q1.pop()
                p_cur = p1.pop()
                
                if q_cur.val != p_cur.val:
                    return False

                if q_cur.left and p_cur.left:
                    q1.appendleft(q_cur.left)
                    p1.appendleft(p_cur.left)
                elif q_cur.left or p_cur.left:
                    return False

                if q_cur.right and p_cur.right:
                    q1.appendleft(q_cur.right)
                    p1.appendleft(p_cur.right)
                elif q_cur.right or p_cur.right:
                    return False

        # if q1 or p1:
        #     return False
        
        return True

