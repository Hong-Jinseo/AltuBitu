# 백준 1316번
# 그룹 단어 체커

n = int(input())
words = []
result = 0

for _ in range(n):
    words.append(input())

for w in words:
    alphabet = ['0']
    temp = 1
    
    for i in range(len(w)):
        # 연속해서 나오지 않았고, 이전에 나왔던 알파벳이라면
        if w[i] != alphabet[-1] and w[i] in alphabet:
            temp = 0
            break
        else:
            alphabet.append(w[i])
            
    if temp == 1:
        result += 1

print(result)
