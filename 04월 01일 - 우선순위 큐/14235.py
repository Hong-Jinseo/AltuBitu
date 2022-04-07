# 백준 14235번
# 크리스마스 선물

import heapq as hq

# max heap
present = []

n = int(input())

for _ in range(n):
    a = input()
    
    if a=='0':
        if present:
            print(-hq.heappop(present))
        else:
            print(-1)

    else:
        li = list(map(int, a.split()))
        
        for i in range(1, len(li)):
            hq.heappush(present, -li[i])
