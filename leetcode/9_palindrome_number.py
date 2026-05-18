import numpy as np

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        x = str(x)
        
        if len(x) == 1: return True
        
        middle = len(x)/2 - 0.5
                
        for i in np.arange(middle, 0, -1):
            if x[int(middle-i)] != x[int(middle+i)]:
                return False
            
        return True