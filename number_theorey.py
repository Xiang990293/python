# fermat's small theorem
# a^p _= a (mod p) #where p is prime number

import math
import itertools

dpprime = set()
dpfactorize = dict()


def combine(n, m):
    for kn in n.keys():
        if kn in m.keys():
            m[kn] += n[kn]
    n.update(m)
    return n

def int_factorize(n):
    
    if n == 0:
        return {}
    if n == 1:
        return {}
    if n == 2 or n == 3:
        dpprime.add(n)
        dpfactorize[n] = {n: 1}
        return {n: 1}
    
    if max(dpprime)*max(dpprime) < n:
        int_factorize(max(dpprime)*max(dpprime)+1)
    
    # print(math.ceil(math.sqrt(n)))
    for i in dpprime:
        if n % i == 0:
            result = combine({i:1}, int_factorize(n//i))
            return result
    return {n: 1}
    
def is_prime(x):
    if x in dpprime:
        return True
    
    dpfactorize[x] = int_factorize(x)
        
    if x == 2 or x == 3:
        dpprime.add(x)
        return True
    
    # print(dpfactorize[x], len(dpfactorize[x].keys()))
    if len(dpfactorize[x].keys()) == 1 and 1 in dpfactorize[x].values():
        dpprime.add(x)
        return True
    return False

            
            
def euler_phi(x):
    if is_prime(x):
        return x-1
    result = 1
    for key, value in dpfactorize[x].items():
        if value == 1:
            result *= key-1
        else:
            result *= (key-1) * key**(value-1)
    return result

def factor_sum(x):
    if x == 0:
        return 0
    prod = 1
    
    try:
        if dpfactorize[x] > 1 :
            pass
    except:
        dpfactorize[x] = int_factorize(x)
        
    
    for prime, count in dpfactorize[x].items():
        sum = 0
        # print(f"{x} -> {prime} => {count}")
        for i in range(count+1):
            sum += prime**i
        prod *= sum
    return prod - x

def gcd(a, b):
    if a == b:
        return a
    if a < b:
        return gcd(b-a, a)
    return gcd(a-b, b)
    
def exgcd(a, b):
    if b == 0:
        return a,1,0
    d, x, y = exgcd(b, a%b)
    return d, y, x - a//b * y
    
    
def china_remainder_theorem(remainder_modulo_pairs):
    modulos=[]
    for remainder, modulo in remainder_modulo_pairs:
        remainders.append(remainder)
        modulos.append(modulo)
        
    not_coprime_modulos=set()
    for pair in itertools.combinations(modulos,2):
        if gcd(*pair) != 1:
            not_coprime_modulos.add(*pair)
            
    if not_coprime_modulos:
        for i in list(not_coprime_modulos):
            modulos.remove(i)
            
            for factor, count in int_factorize(i).items():
                modulos.append(factor)
    

    remainders=[]
    Modprod=[]
    result=0
    for remainder, modulo in remainder_modulo_pairs:
        remainders.append(remainder)
        modulos.append(modulo)
    
    M=math.prod(modulos)
    for remainder, modulo in remainder_modulo_pairs:
        Mi=M//modulo
        d, x, y = exgcd(Mi, modulo)
        while x < 0:
            x += modulo
            
        result+=remainder*x*Mi
        
    while result >= M:
        result -= M
    
    return result


int_factorize(2)
int_factorize(3)

print(exgcd(1001, 9600))

# print(int_factorize(
# 765434576345637173823138479813768765238613741311236937264827654778277325473898928152422542515522536131313315113131436465191945461216494600604573790464767487277872182954748299792393745245635321521251762851642417215462185215216524128156631535133635135624373234146484945914624245144655937545243151552364728646254632586421653765268752146364216452966051582166316165298691556167867525411656512513466425667026216616514563466741256352312000214153442514256547456176523156416857441156514555136515571345216351461342355314575145551352534665275245434123524164512514854135513552515115617195661675681735681361373613725382416248275264278352381658327184562416554631567452166375415676516659156451553145235234613252553232516852127126451621572321315221367251321433642212341623226546564323221637261423214278263167424542351254254143654215461524423554259418149422453565065652624639606225635206461462565251661258214063232062267640333141325426372633225334823727365243212325634253834253324362370285630743325310023223052360452321456631647857143521514557163023223522423243624702260270285607962516432235723674724715613526215523165518237142314221623715637261634153471
# ))
#print(china_remainder_theorem([(7,2**5),(2,3**2),(7,5),(2,7)]))