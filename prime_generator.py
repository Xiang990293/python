import math
import random

def is_fermat_prime_candidate(p, a_list):
    # 檢查p是否大於1且為整數
    if p <= 1:
        return False
    for a in a_list:
        # 若a與p不互質，跳過此a（因為費馬小定理要求gcd(a,p)=1）
        if gcd(a, p) != 1:
            continue
        # 計算a^(p-1) mod p
        if pow(a, p-1, p) != 1:
            return False
    return True

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 範例：找出範圍內符合條件的p
def find_p_candidates(start_p, end_p, a, candidates_length = 2, condition = lambda : True):
    a_list = [a + i for i in range(6)]  # a, a+1, ..., a+5
    for p in range(start_p, end_p + 1):
        print(p)
        candidates = []
        if is_fermat_prime_candidate(p, a_list):
            candidates.append(p)
            if candidates_length == 1:
                return p
        if candidates_length == len(candidates):
            try:
                if condition(*candidates):
                    return candidates
                else:
                    candidates.clear()
                    continue
            except:
                print("condition function wrong")
            
            

if __name__ == "__main__":
    setting = input("請輸入模式: 0.預設 1.自訂模式 2.孿生質數模式\n")
    
    if setting == "1":
        digits = int(input("請輸入質數位數: "))
        count = int(input("請輸入p的個數: "))
    elif setting == "2":
        digits = int(input("請輸入質數位數: "))
        count = 1
        candidates_length = 2
        condition = lambda x, y: abs(x - y) == 2
    else:
        digits = 20
        count = 2
        candidates_length = 2
        
            
    # 使用範例
    a = random.randint(1,10**(digits-1))
    for _ in range(count):
        temp=""
        for i in range(digits):
            temp+=str(random.randint(0, 9))
        start_p = int(temp)
        end_p = start_p +1000
        result = find_p_candidates(start_p, end_p, a, candidates_length, condition)
        print(f"{_+1}: {result}")