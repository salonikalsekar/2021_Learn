class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for root in lists:
            while root:
                heappush(minHeap, root.val)
                root = root.next

        res = node = ListNode(0)
        i = 0
        l = len(minHeap)
        while i < l:
            t = heapq.heappop(minHeap)
            res.next = ListNode(t)
            i += 1
            res = res.next

        return node.next