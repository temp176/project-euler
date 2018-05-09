import numpy as np

def isPrime(N):
    for i in range(2,int(np.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

total = 0
N = [i for i in range(2,2000000) if i % 2 != 0 and i % 5 != 0]
for i in range(len(N)):
    if isPrime(int(N[i])):
        total = total + int(N[i])
print(total+7)