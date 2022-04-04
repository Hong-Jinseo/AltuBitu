# 파이썬 11053번
# 가장 긴 증가하는 부분 수열

n = int(input())
a = list(map(int, input().split()))

dp = [1 for _ in range(n)]

# LIS 알고리즘
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)
                
print(max(dp))
