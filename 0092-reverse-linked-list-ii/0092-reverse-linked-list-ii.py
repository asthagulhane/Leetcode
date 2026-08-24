class Solution:

    def reverseBetween(                                                                         
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        
        vals = []  
        curr = head                                                                                               
        while curr:
            vals.append(curr.val)
            curr = curr.next

        vals[left - 1 : right] = vals[left - 1 : right][::-1]
    
        curr = head
        for val in vals:
            curr.val = val
            curr = curr.next

        return head

        
        