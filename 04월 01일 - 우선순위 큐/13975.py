# 백준 13975번
# 파일 합치기 3

import heapq as hq
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    k = int(input())
    file_size = list(map(int, input().split()))
    cost = []

    # 최소힙 
    for fs in file_size:
        hq.heappush(cost, fs)

    # 사이즈가 가장 작은 파일 두 개를 합쳐서 다시 힙에 저장
    total = 0
    while len(cost) > 1: # 힙에 남아있는 데이터가 2개 이상인 경우
        temp = hq.heappop(cost) + hq.heappop(cost)
        hq.heappush(cost, temp)
        total += temp

    print(total)
