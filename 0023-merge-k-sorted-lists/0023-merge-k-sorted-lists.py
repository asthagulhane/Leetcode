class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, head in enumerate (lists):
            if head:
               heapq.heappush(heap, (head.val, i, head))

        dummy = ListNode(0)     
        current = dummy 

        while heap:
            val, i, node = heapq.heappop(heap) 
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next        
        