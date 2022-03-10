#백준 1026번
#보물

N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

s = 0

a_list.sort()
b_list.sort(reverse=True)

for i in range(N):
    s += a_list[i] * b_list[i]
    
print(s)