class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        
        # Initialize frontiers for both directions
        front, back = {beginWord}, {endWord}
        length = 1
        
        while front and back:
            # Always expand the smaller frontier to minimize operations
            if len(front) > len(back):
                front, back = back, front
                
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nxt = word[:i] + c + word[i+1:]
                        
                        # Connection found between both frontiers
                        if nxt in back:
                            return length + 1
                        
                        # Valid unvisited word found
                        if nxt in words:
                            words.remove(nxt)
                            next_front.add(nxt)
                            
            front = next_front
            length += 1
            
        return 0
