#백준 18115번
#카드 놓기

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stack = list(map(int, input().split()))
card = deque()

for i in range(N):
    top = stack.pop()
    if top == 1:
        card.appendleft(i+1)
    elif top == 2:
        card.insert(1, i+1)
    elif top == 3:
        card.append(i+1)

for i in card:
    print(i, end=' ')