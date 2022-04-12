# 백준 1080번
# 행렬

def calc_matrix(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j]
        

n, m = map(int, input().split())
a, b = [], []

for i in range(n): a.append(list(map(int, input())))
for i in range(n): b.append(list(map(int, input())))

# 행렬a와 행렬b의 원소를 순차적으로 비교
cnt = 0
for p in range(n-2):
    for q in range(m-2):
        # a와 b의 원소가 다르다면 연산 실행
        if a[p][q] != b[p][q]:
            calc_matrix(p, q)
            cnt += 1

# 연산이 끝난 행렬 a가 b와 동일한지 확인
result = True
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            result = False
            break

if result == True:
    print(cnt)
else:
    print(-1)
