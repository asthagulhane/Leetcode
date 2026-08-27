class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        
        # Populate the queues with initial indices
        for i, char in enumerate(senate):
            if char == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        # Simulate the voting process round by round
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            # The senator with the smaller index bans the opponent
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
                
        return "Radiant" if radiant else "Dire"
