# 백준 9084번
# 동전

t = int(input())

for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    able = [0 for _ in range(m+1)]
    able[0] = 1

    # 낼 수 있는 동전 c
    for c in coin:
        # 동전으로 만들 금액 i
        for i in range(1, m+1):
            if i-c >= 0:                # 동전의 액면가 <= 동전으로 만들 금액
                able[i] += able[i-c]    # able[i] = able[i] + (able[i-c] + c원)

    print(able[m])
