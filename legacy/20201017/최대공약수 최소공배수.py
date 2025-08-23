from collections import deque
import copy
from itertools import combinations, permutations

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
print(gcd(5, 10))

def lcm(x, y):
    return x * y // gcd(x, y)
print(lcm(10, 4))