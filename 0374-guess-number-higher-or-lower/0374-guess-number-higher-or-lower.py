class Solution:

    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            res =   guess(mid)  # Pre-defined API call

            if res == 0:
                return mid
            elif res == 1:
                low = mid + 1  # Guess is lower, look higher
            else:
                high = mid - 1  # Guess is higher, look lower
