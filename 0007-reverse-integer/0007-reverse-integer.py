class Solution:
    def reverse(self, x: int) -> int:
        if x< 0:
            val = - int(str(abs (x)) [::-1])
        else :
            val = int(str(x) [::-1])
        if -2**31 <= val <= 2**31 - 1:
            return val 
        return 0

    
       
          