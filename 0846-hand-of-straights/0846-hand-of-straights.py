class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # Total cards must be perfectly divisible by the group size
        if len(hand) % groupSize != 0:
            return False
            
        count = Counter(hand)
        
        # Process cards from smallest to largest
        for card in sorted(count.keys()):
            if count[card] > 0:
                needed = count[card]
                # Check and consume the next consecutive groupSize cards
                for i in range(card, card + groupSize):
                    if count[i] < needed:
                        return False
                    count[i] -= needed
                    
        return True
