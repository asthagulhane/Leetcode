class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        
        for right in range(len(s)):
            # Update frequency of the current character
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Maintain the peak historical frequency in the current window sequence
            max_freq = max(max_freq, count[s[right]])
            
            # If current_window_size - max_freq > k, the window is invalid
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
        # The maximum window size ever achieved is exactly the valid answer
        return len(s) - left
