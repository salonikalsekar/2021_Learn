# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersect(self, head: ListNode) -> ListNode:
        tortoise = head
        hare = head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise

        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return

        ptr2 = self.getIntersect(head)
        if not ptr2:
            return None

        ptr1 = head

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1