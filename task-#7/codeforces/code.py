#1

import math

def theatresquare(n, m, a):
    
    r = math.ceil(n / a)
    c = math.ceil(m / a)
    flagstones = r * c
    return flagstones


n, m, a = map(int, input("Enter n, m, and a: ").split())

result = theatresquare(n, m, a)
print("Number of flagstones required:", result)
