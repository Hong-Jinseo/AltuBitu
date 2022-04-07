# 백준 12018번
# Yonsei TOTO

import heapq as hq

# 리스트의 원소들에 -1을 곱한 새로운 리스트로 반환
def mul_minus_one(li):
    temp = []
    for i in li:
        temp.append(-i)
    return temp


acc = []    # 성준의 마일리지

n, m = map(int, input().split())            # 과목 수 n, 주어진 마일리지 m

for _ in range(n):
    p, l = map(int, input().split())        # 신청한 사람 수 p, 수강 인원 l

    temp = list(map(int, input().split()))  # 각 사람이 넣은 마일리지
    mileage = mul_minus_one(temp)           # 최대힙을 만들기 위해 -1 곱해줌
    hq.heapify(mileage)
    
    # 수강신청 인원 >= 수강 정원
    if len(mileage) >= l:
        for _ in range(l):
            val = hq.heappop(mileage)
        acc.append(val)
    # 수강신청 인원 < 수강 정원
    else:
        acc.append(-1)


acc = mul_minus_one(acc)
acc.sort()
total = cnt = 0

for i in acc:
    if total + i <= m:
        total += i
        cnt += 1
    else:
        break

print(cnt)
        
