class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = r = 0
        if root.left:
            l = self.maxDepth(root.left)
        if root.right:
            r = self.maxDepth(root.right)

        return max(l, r) + 1
