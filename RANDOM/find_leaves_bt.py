from collections import defaultdict


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        def traverse(node, t):
            l = r = 0
            if node.left:
                l = traverse(node.left, t)
            if node.right:
                r = traverse(node.right, t)

            length = max(l, r)
            t[length].append(node.val)

            return length + 1

        t = defaultdict(list)
        traverse(root, t)
        return t.values()