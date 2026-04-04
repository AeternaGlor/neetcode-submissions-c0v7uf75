# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        if not root: return ""
        q = collections.deque([root])

        while q:
            curr = q.pop()
            if not curr:
                res.append("N")
                continue
            res.append(str(curr.val))
            q.appendleft(curr.left)
            q.appendleft(curr.right)
        # print(res)
        return ",".join(res)


    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(",")

        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 0
        while q:
            curr = q.pop()
            if nodes[i+1] == "N":
                curr.left = None
            else:
                curr.left = TreeNode(int(nodes[i+1]))
                q.appendleft(curr.left)
            i += 1
            
            if nodes[i+1] == "N":
                curr.right = None
            else:
                curr.right = TreeNode(int(nodes[i+1]))
                q.appendleft(curr.right)
            i += 1
            
        return root
            
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))