# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        curr = head
        n = 1
        new_tail = head

        while curr.next:
            curr = curr.next
            n += 1

        curr.next = head

        for i in range(n - k % n - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        new_tail.next = None

        return new_head
