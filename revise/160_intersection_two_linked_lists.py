class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        newA = headA
        newB = headB

        while newA != newB:
            if not newA:
                newA = headB
            else:
                newA = newA.next
            if not newB:
                newB = headA
            else:
                newB = newB.next
        return newA