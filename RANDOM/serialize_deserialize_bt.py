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

        def preorder(node):
            l = []
            r = []
            if not node:
                return [None]

            l = preorder(node.left)
            r = preorder(node.right)

            return [node.val] + l + r

        res = [str(i) for i in preorder(root)]
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        q = data.split(',')

        def buildTree(q):
            curr = q.pop(0)
            if curr == 'None':
                return
            else:
                newn = TreeNode(int(curr))
                newn.left = buildTree(q)
                newn.right = buildTree(q)

            return newn

        return buildTree(q)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))