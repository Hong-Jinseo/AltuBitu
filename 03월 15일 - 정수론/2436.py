# 백준 2436번
# 공약수

def get_gcd(a, b):
    # a > b
    while b != 0:
        a %= b
        a,b = b,a
    return a


# 최대공약수 GCD, 최소공배수 LCM
gcd, lcm = map(int, input().split())
temp = 1

# a * b = LCM // GCD
ab = lcm//gcd

sqrt_ab = int(ab ** (1/2))

for z in range(sqrt_ab, 1, -1):
    # z는 ab의 약수, z와 ab/z는 서로소
    if ab%z == 0 and get_gcd(z, ab/z) == 1:
        temp = z
        break

# A = a * GCD, B = b * GCD
print(temp * gcd, ab//temp * gcd)
