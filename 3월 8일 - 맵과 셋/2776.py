#백준 2776번
#암기왕

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    a_list = set(map(int, input().split()))

    M = int(input())
    b_list = list(map(int, input().split()))

    for i in b_list:
        if i in a_list:
            print(1)
        else:
            print(0)