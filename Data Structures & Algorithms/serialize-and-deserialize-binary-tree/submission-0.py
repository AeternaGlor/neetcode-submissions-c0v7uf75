# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                return 0
            right_nodes = dfs(root.right)
            left_nodes = dfs(root.left)
            
            res.append(str(root.val) + "l" + str(left_nodes) + "r" + str(right_nodes) + "_")
            return 1 + left_nodes + right_nodes
        
        dfs(root)
        res = "".join(res[::-1])
        # 1l1r3_2l0r0_3l1r1_4l0r0_5l0r0_
        return res

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        nodes = []
        i = 0
        while i < len(data):
            val = ""
            while data[i] != "l":
                val += data[i]
                i += 1
            i += 1
            left_nodes = ""
            while data[i] != "r":
                left_nodes += data[i]
                i += 1 
            i += 1
            right_nodes = ""
            while data[i] != "_":
                right_nodes += data[i]
                i += 1 
            i += 1
            nodes.append((int(val), int(left_nodes), int(right_nodes)))
        # print(nodes)
        # [(1, 1, 3), (2, 0, 0), (3, 1, 1), (4, 0, 0), (5, 0, 0)]

        def build_tree(l, r):
            if l > r:
                return None
            root_val, l_nodes, r_nodes = nodes[l]
            
            root = TreeNode(root_val)

            root.left = build_tree(l + 1, l + l_nodes)
            root.right = build_tree(l + l_nodes + 1, r)

            return root
        
        return build_tree(0, len(nodes) - 1)

            
            
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))