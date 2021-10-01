class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        maxVal = float('-inf')
        self.c = 0

        def dfs(node, maxVal):
            if node:
                if node.val >= maxVal:
                    maxVal = node.val
                    self.c += 1

                dfs(node.left, maxVal)
                dfs(node.right, maxVal)

        dfs(root, maxVal)
        return self.c