# 백준 1205번
# 등수 구하기

import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 1,000,000번으로
input = sys.stdin.readline


def check_rank(rank, score):
    r = rank
    if rank == n or ranking[rank] <= score:
        return rank
    else:
        r = check_rank(rank+1, score)
        return r


# 저장된 개수, 태수의 점수, 저장 가능 개수
n, s, p = map(int, input().split())

if n>0:
    ranking = list(map(int, input().split()))

    if n==p and ranking[-1]>=s:
        print(-1)
    else:
        r = check_rank(0, s)
        print(r+1)
else:
    print(1)
