import math

class Solution:
    def reverse(self, x: int) -> int:
        isnegative = x < 0
        
        x = abs(x)
        
        x = int(str(x)[::-1])
        # digits = int(math.log10(x)) + 1
        
        if x > 2**31 - 1 or x < -2**31: return 0
        
        return -x if isnegative else x
    
print(Solution().reverse(120))