#백준 11478번
#서로 다른 부분 문자열의 개수

str = input()
s = set()

for i in range(0, len(str)):
    for j in range(i+1, len(str)+1):
        s.add(str[i:j])

print(len(s))