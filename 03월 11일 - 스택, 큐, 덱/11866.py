#백준 11866번
#요세푸스 문제 0

from collections import deque

n, k = map(int, input().split())

deq = deque(i+1 for i in range(n))

print('<', end='')
while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())   # deq의 왼쪽에서 삭제한 값을 오른쪽으로 삽입 (k-1번 반복)

    print(deq.popleft(), end='')    # k번째 값 출력
    if deq:
        print(', ', end='')         # 마지막 값이 아니라면 쉼표 출력 
print('>')  
