from math import inf
from Probe_4_11 import a,b
def divide(first, second):
    first = int(a)
    second = int(b)
    if second == 0:
        return inf
    else:
        res = first / second
        return res

print(divide(a, b))
