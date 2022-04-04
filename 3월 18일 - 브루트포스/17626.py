# 백준 17626번
# Four Squares

import sys
input = sys.stdin.readline

n = int(input())

count = [4 for i in range(n+1)]

for k in range(int(n**(1/2))+1):
    count[k*k] = 1

for i in range(1, n+1):
    for j in range(1, int(i**(1/2))+1):

        # 제곱수만 사용할 수 있기 때문에 (n**2)의 경우만 고려함
        # ex) count[12] = count[12-1] + 1 = count[12-4] + 1 = count[12-9] + 1
        # ex) count[12]는 특정한 x에 1**2, 2**2, 3**2 를 더한 수로 구성됨
        
        if count[i] > count[i - j*j] + 1:
            count[i] = count[i - j*j] + 1
    
print(count[n])
