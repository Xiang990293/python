import itertools
import math
import numpy as np

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result = None
        result_margin = None
        half_len = len(s)/2                                       # half the length of the string
        half_index = half_len-0.5                                 # the index of the middle character
        
        for i in np.arange(0.0, len(s)-0.5, 0.5):
            max_margin_middle = half_index - abs(i - half_index) # the margin for the current positio
            
            # print(np.arange(0.0, len(s)-0.5, 0.5),"*",np.arange(max_margin_middle, -0.50, -1)[::-1])
            for j in np.arange(max_margin_middle, -0.50, -1)[::-1]:
                # print(i, j, result, result_margin, i < j)
                if s[int(i-j)] == s[int(i+j)]: 
                    if (not result) or (result_margin < j):
                        # print(result, s[int(i-j):int(i+j+1)])
                        result = s[int(i-j):int(i+j+1)]
                        result_margin = j
                else: break
                    
        return result
    
print(Solution().longestPalindrome("())("))