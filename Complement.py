import math
from math import log2
x = 55
n = math.floor(log2(x)) + 1

bitmask = (1 << n) - 1
print(bitmask)
print(bin(bitmask ^ x))
