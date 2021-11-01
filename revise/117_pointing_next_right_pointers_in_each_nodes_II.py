class Solution:
    def connect(self, root: 'Node') -> 'Node':

        q = []
        if not root:
            return
        q.append([root])

        while q:
            curr = q.pop(0)

            level_children = []

            for n in curr:
                if n.left:
                    level_children.append(n.left)
                if n.right:
                    level_children.append(n.right)

            if len(level_children) > 0:
                for i in range(len(level_children) - 1):
                    level_children[i].next = level_children[i + 1]
                q.append(level_children)

        return root