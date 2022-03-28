# 백준 1009번
# 분산처리

T = int(input())

last_digit = [[] for i in range(11)]

for j in range(1, 10):
    num = j
    while num not in last_digit[j]:
        last_digit[j].append(num)
        
        num *= j
        num %= 10


for _ in range(T):
    a, b = map(int, input().split())

    if a%10 == 0:
        print(10)
    else:
        ld = a % 10
        length = len(last_digit[ld])
        print(last_digit[ld][b%length-1])
