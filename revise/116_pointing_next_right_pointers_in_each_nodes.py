class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        q = [[root]]
        # q = []
        # if not root:
        #     return
        # q.append([root])
        while q:
            level_children = []
            curr = q.pop(0)
            for c in curr:

                if c.left:
                    level_children.append(c.left)
                if c.right:
                    level_children.append(c.right)

            if len(level_children) > 0:
                for i in range(len(level_children) - 1):
                    level_children[i].next = level_children[i + 1]

                q.append(level_children)

        return root
