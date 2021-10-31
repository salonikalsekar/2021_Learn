class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev