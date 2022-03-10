#백준 11651번
#좌표 정렬하기 2

import sys

coord = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

coord.sort(key=lambda z : (z[1], z[0]))
# key : 정렬 기준
# 정렬 1순위 기준 : y좌표 기준으로 오름차순
# 정렬 2순위 기준 : x좌표 기준으로 오름차순

for i in coord:
    print(i[0], i[1]) #튜플에 속한 값 출력