class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length and the tail node
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
            
        # Step 2: Handle rotations larger than length
        k = k % length
        if k == 0:
            return head
            
        # Step 3: Connect tail to head to make it circular
        tail.next = head
        
        # Step 4: Find the new tail (length - k steps from head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # Step 5: Break the ring and set the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
