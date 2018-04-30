#参考：http://szarny.hatenablog.com/entry/2017/09/21/232855#%E7%B4%A0%E6%95%B0%E3%81%AE%E6%80%A7%E8%B3%AA%E3%82%92%E5%88%A9%E7%94%A8%E3%81%97%E3%81%9F%E5%88%A4%E5%AE%9A%E6%B3%95
import numpy as np

def isPrime(N):
    for i in range(2,int(np.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

count = 0
i = 0
while count < 10002:
    i += 1
    if isPrime(i):
        count += 1
print(i)