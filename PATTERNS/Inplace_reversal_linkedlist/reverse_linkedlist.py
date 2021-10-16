class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev