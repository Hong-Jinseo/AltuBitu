#백준 20291번
#파일 정리

dic = dict()
n = int(input())

for i in range(n):
    name, extension = input().split('.')

    if extension in dic:
        dic[extension] += 1
    else:
        dic[extension] = 1

for key, value in sorted(dic.items()):
    print(key, value)