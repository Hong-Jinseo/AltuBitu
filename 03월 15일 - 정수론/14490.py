# 백준 14490번
# 백대열

n, m = map(int, input().split(':'))
gcd, temp = n, m

while temp != 0:
    gcd %= temp
    gcd, temp = temp, gcd

print('%d:%d' %(n//gcd, m//gcd))
