#백준 2841번
#외계인의 기타 연주

from collections import deque
import sys
input = sys.stdin.readline

n, p = map(int, input().split())
count = 0

play = deque(tuple(map(int, input().split())) for _ in range(n))    #입력값
stack = [[] for _ in range(n+1)]    # n개의 스택을 저장할 2차원 리스트

while play:
    temp = play.popleft()
    # temp[0] : 줄 번호
    # temp[1] : 프랫 번호

    # 스택이 빈 경우
    if not stack[temp[0]]:
        stack[temp[0]].append(temp[1])
        count += 1 
        continue
    
    # top < new (스택의 top이 새로운 값보다 작을 경우)
    if stack[temp[0]][-1] < temp[1]:
        stack[temp[0]].append(temp[1])
        count += 1
    
    # top = new
    elif stack[temp[0]][-1] == temp[1]:
        continue

    # top > new
    elif stack[temp[0]][-1] > temp[1]: 
        while stack[temp[0]] and stack[temp[0]][-1]>temp[1]:
            stack[temp[0]].pop()
            count += 1
            
        if stack[temp[0]] and stack[temp[0]][-1] == temp[1]:
            continue

        stack[temp[0]].append(temp[1])
        count += 1

print(count)

