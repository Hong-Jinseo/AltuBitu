# 백준 11727번
# 2xn 타일링 2

n = int(input())
dp = [0, 1, 3]

for i in range(3, n+1):
    # i) dp[i-1]에 1x2 타일을 붙인 경우
    # ii) dp[i-2]에 2x1 타일을 2개 붙인 경우
    # iii) dp[i-2]에 2x2 타일을 붙인 경우
    dp.append(dp[i-1] + dp[i-2]*2)

print(dp[n] % 10007)
