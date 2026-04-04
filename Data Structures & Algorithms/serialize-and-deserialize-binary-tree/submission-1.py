# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return

            res.append(str(root.val))

            dfs(root.left)
            dfs(root.right)
            return
        
        dfs(root)
        return ",".join(res)

        

    def deserialize(self, data):
        if not data:
            return None
        
        nodes = data.split(",")

        i = 0
        def dfs():
            nonlocal i
            if nodes[i] == "N":
                i += 1
                return None
            root = TreeNode(int(nodes[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()

            
            
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))