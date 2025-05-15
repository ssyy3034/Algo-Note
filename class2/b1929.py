import math
n,m = map(int, input().split())
isPrime = True

def primecheck(k):
    root_k = math.sqrt(k)
    for i in range(2, int(root_k)+1):
        if k % i == 0:
            return False
    return True
for i in range(n,m):
    if primecheck(i):
        print(i)


