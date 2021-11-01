class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node: return 0
            l, r = dfs(node.left), dfs(node.right)
            self.ans += abs(l) + abs(r)

            return l + r + node.val - 1

        dfs(root)
        return self.ans