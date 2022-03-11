#백준 20291번
#파일 정리

dic = dict()
n = int(input())

for i in range(n):
    name, extension = input().split('.')    #파일명과 확장자를 분리

    if extension in dic:        #확장자가 dic에 있으면
        dic[extension] += 1     #value값 1 추가 (나온 횟수)
    else:                       
        dic[extension] = 1      

for key, value in sorted(dic.items()):      #사전 순 정렬
    print(key, value)