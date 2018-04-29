#参考：https://note.nkmk.me/python-gcd-lcm/

import math
from functools import reduce

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

reduce(lcm,range(1,21))