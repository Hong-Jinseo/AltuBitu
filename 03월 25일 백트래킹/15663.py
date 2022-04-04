# 백준 15663번
# N과 M

import itertools
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

arr = list(set(itertools.permutations(num, m)))
arr.sort()

for a in arr:
    print(*a)
