# 백준 11723번
# 집합

import sys
input = sys.stdin.readline

m = int(input())
S = [False for _ in range(21)]

for _ in range(m):
    temp = input().rstrip()
    
    if ' ' in temp:
        op, n = temp.split(' ')
        n = int(n)

        if op=='add':
            S[n] = True

        elif op=='remove':
            S[n] = False

        elif op=='check':
            if S[n]==True:
                print('1')
            else:
                print('0')

        elif op=='toggle':
            if S[n]==True:
                S[n] = False
            else:
                S[n] = True

    elif temp=='all':
        S = [True for _ in range(21)]
    else:
        S = [False for _ in range(21)]
