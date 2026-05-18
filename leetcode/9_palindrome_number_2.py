class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        x = str(x)
        
        if len(x) == 1: return True
        
        is_even_number_of_digits = len(x) % 2 == 0