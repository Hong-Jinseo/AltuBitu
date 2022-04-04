# 백준 14888번
# 연산자 끼워넣기

# 백트래킹이 맞나...?

import itertools
import sys
input = sys.stdin.readline

def calc(n1, n2, op):
    # 덧셈, 뺼셈, 곱셈, 나눗셈 순
    if op==0: return n1+n2
    elif op==1: return n1-n2
    elif op==2: return n1*n2
    else:
        if n1<0 and n2>0:
            n1 *= -1
            return -1*(n1//n2)
        else:
            return n1//n2


n = int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split()))

oper = []
num_set = set()

# 연산자 모든 경우의 수
for i in range(4):
    for j in range(op[i]):
        oper.append(i)
oper = set(itertools.permutations(oper))

for operator in oper:
    number = num[:]
    for k in range(n-1):
        if operator[k]!=3 or number[k+1]!=0:
            number[k+1] = calc(number[k], number[k+1], operator[k])
    num_set.add(number[-1])

print(max(num_set))
print(min(num_set))
