# 백준 13305번
# 주유소

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_p = price[0]     # 가장 저렴한 기름값
total_p = 0

# 마지막 마을의 기름값 정보는 필요 없기 때문에 zip으로 묶어도 문제 없음
for d,p in zip(distance, price):
    if min_p > c:
        min_p = c           # 가장 저렴한 기름값 갱신
    total_p += min_p*d      # 최소 기름값 * 거리

print(total_p)
