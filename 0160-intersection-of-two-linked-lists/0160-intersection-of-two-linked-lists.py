class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        
        while pA != pB:
            # If pointer reaches the end, redirect to the other list's head
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
            
        return pA
