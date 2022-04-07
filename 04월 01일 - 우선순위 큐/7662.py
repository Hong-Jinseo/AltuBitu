# 백준 7662번
# 이중 우선순위 큐

# 25퍼 인덱스 에러

import heapq as hq
import sys
input = sys.stdin.readline


# root의 value가 false면 heap에서 삭제하는 함수
def synchronize(heap, li):
    while heap and not li[heap[0][1]]:
        hq.heappop(heap)
    return heap, li


# 입력받은 heap의 root를 삭제하는 함수
def delete_root(heap, li):
    heap, li = synchronize(heap, li)
    
    if heap:
        li[heap[0][1]] = False
        pop = hq.heappop(heap)
        
    return heap, li


t = int(input())     

for _ in range(t):
    k = int(input())
    
    min_heap = []
    max_heap = []
    value = [False for _ in range(k+1)]     # heap에 있는 값이면 True, 아니면 False
        
    for i in range(k):
        cmd, num = input().split()
        num = int(num)

        if cmd=='I':
            hq.heappush(min_heap, (num, i))     # (우선순위, 값) 
            hq.heappush(max_heap, (-num, i))
            value[i] = True

        elif cmd=='D' and min_heap and max_heap:
            if num==1:
                max_heap, value = delete_root(max_heap, value)
            else:
                min_heap, value = delete_root(min_heap, value)

    # root(최댓값 또는 최솟값) 출력 전 동기화
    max_heap, value = synchronize(max_heap, value)
    min_heap, value = synchronize(min_heap, value)

    if not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])
