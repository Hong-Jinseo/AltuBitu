# 백준 6588번
# 골드바흐의 추측

import sys

MAX = 1000000

prime = [True for i in range(MAX+1)]
prime[0] = prime[1] = False

for i in range(2, int(MAX**(1/2))+1):
   for j in range(i*i, MAX+1, i):
       prime[j] = False


while True:
    n = int(sys.stdin.readline())

    if n==0: break

    for k in range(3, len(prime)):
        if prime[k] and prime[n-k]:
            print('%d = %d + %d' %(n, k, n-k))
            break
