class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        for i in range(0, len(nodes) - len(nodes) % k, k):
            nodes[i:i+k] = reversed(nodes[i:i+k])

        dummy = ListNode(0)      
        curr = dummy 
        for node in nodes:
            curr.next = node
            curr = curr.next
        curr.next = None

        return dummy.next    
        