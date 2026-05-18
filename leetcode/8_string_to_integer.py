class Solution:
    def myAtoi(self, s: str) -> int:
        map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        
        if s == "":
            return 0
        
        while s[0] == " ":
            s = s[1::]
            if s == "":
                return 0
        
        isNegative = False
        if s[0] == "-":
            isNegative = True
            s = s[1::]
        elif s[0] == "+":
            s = s[1::]
            
        if s == "":
            return 0
            
        for i, c in enumerate(s):
            if c not in map:
                s = s[:i:]
                
        
        reversed_s = s[::-1]
        
        result = 0
        power = 0
        if not isNegative:
            for c in reversed_s:
                if c in map:
                    result += map[c] * 10**power
                    power += 1
                else:
                    break
            while result > 2**31-1:
                result= 2**31-1
        else:
            for c in reversed_s:
                if c in map:
                    result -= map[c] * 10**power
                    power += 1
                else:
                    break
            while result < -2**31:
                result= -2**31
        
        return result
    
