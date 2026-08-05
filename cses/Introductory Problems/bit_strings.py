n = int(input())

'''
#as condition shows:
#   1 <= n <= 10**6
#   
#   so yeah, no way this doing anything
#   Sorry, Fermat.

critical_1 = 10**9+6

if n >= critical_1:
    n = n % critical_1
'''

j = 1
for i in range(n):
    j *= 2
    if j > 10**9+7:
        j -= 10**9+7
print(j)

"""
447
941778035
"""
