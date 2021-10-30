# 1
# | \
# 2   3
# | \ | \
# _ 4 5  6
# 1
# | \
# 3   2
# | \ | \
# 6 5 4  _

# q = [[2,3]]


# q = [4]
# pop
# [2, 3]
# for 2
# swap
# for elem at that level - push child in another array - add it to q
# left , right - swap
# one of this  - none
class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def reverse_tree(self, root):
        if not root:
            return root

        q = [root]

        while q:
            curr = q.pop()

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return root

# 1
# | \
# 2   3
# | \ | \
# _ 4 5  _
# 1
# | \
# 2   3
# | \ | \
# 4 5 _  _

# 0 - 1
# 1 - 2, 3
# 2 - 4 5








