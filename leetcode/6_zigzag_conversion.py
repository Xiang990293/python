class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        result = ""
        half_divisor = numRows-1
        divisor = (numRows-1) * 2
        
        result = "".join([c for i, c in enumerate(s) if (i % divisor == 0)])
        for j in range(1, half_divisor):
            result += "".join([c for i, c in enumerate(s) if i % divisor == j or i % divisor == (divisor - j)])
        result += "".join([c for i, c in enumerate(s) if (i % divisor == half_divisor)])
        
        return result
    
print(Solution().convert("PAYPALISHIRING", 4))