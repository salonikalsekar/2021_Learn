"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode

        curr = head

        while True:

            if curr.val <= insertVal <= curr.next.val:
                break

            if curr.val > curr.next.val and (curr.val <= insertVal >= curr.next.val):
                break
            elif curr.val > curr.next.val and (curr.val >= insertVal <= curr.next.val):
                break

            curr = curr.next

            if curr == head:
                break

        new_node = Node(insertVal)
        tmp = curr.next
        curr.next = new_node
        new_node.next = tmp
        return head