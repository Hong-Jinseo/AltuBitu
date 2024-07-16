#백준 9375번
#패션왕 신해빈

t = int(input())
c_dict = dict()     #옷 딕셔너리

cnt = 1             #입을 수 있는 조합의 종류

for _ in range(t):
    for _ in range(int(input())):
        c, t = input().split()      #옷의 이름과 종류(type)를 구분
        if t in c_dict:             #해당 type이 딕셔너리에 있으면
            c_dict[t] += 1          #value값 1 추가
        else:                       #없으면
            c_dict[t] = 1           #value값 = 1

    for key in c_dict:
        cnt *= c_dict.get(key) + 1      # 옷의 개수 + 1(안 입은 경우)

    print(cnt - 1)  # 모든 조합 - 1(아무것도 안 입은 경우)

    c_dict.clear()
    cnt = 1
