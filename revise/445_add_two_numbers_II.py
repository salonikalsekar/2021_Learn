# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rl1 = self.reverseList(l1)
        rl2 = self.reverseList(l2)

        carry = 0
        n = res = ListNode(0)
        while rl1 or rl2 or carry:

            if rl1:
                carry += rl1.val
                rl1 = rl1.next
            if rl2:
                carry += rl2.val
                rl2 = rl2.next

            n.next = ListNode(carry % 10)
            carry = carry // 10
            n = n.next

        if carry:
            n.next = ListNode(carry % 10)

        return self.reverseList(res.next)

    def reverseList(self, llist):
        curr = llist
        prev = None
        while llist:
            temp = llist.next
            llist.next = prev
            prev = llist
            llist = temp

        return prev

