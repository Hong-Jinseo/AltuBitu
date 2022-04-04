# 백준 10757번
# 큰 수 A+B

a, b = input().split()

a_list = [i for i in a[::-1]]
b_list = [i for i in b[::-1]]
result = []
temp = 0

if len(a)>=len(b):
    gap = len(a)-len(b)
    for _ in range(gap):
        b_list.append(0)      
else:
    gap = len(b)-len(a)
    for _ in range(gap):
        a_list.append(0)


for n, m in zip(a_list, b_list):
    temp = temp + int(n) + int(m)

    if temp<10:
        result.append(temp)
        temp = 0
    else:
        result.append(temp % 10)
        temp = 1


if temp==1:
    result.append('1')
    temp=0

print(''.join(str(s) for s in result[::-1]))
