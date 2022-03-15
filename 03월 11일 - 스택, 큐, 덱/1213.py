#백준 1213번
#팰린드롬 만들기

a_dict = dict()
odd = 0
odd_alphabet = ''
word = ''

# 각 알파벳 별 개수를 a_dict에 저장
for i in str(input()):    
    if i in a_dict:
        a_dict[i] += 1
    else:
        a_dict[i] = 1

# 알파벳 사전순 정렬
a_dict = dict(sorted(a_dict.items()))

# 앞부분에 나올 알파벳을 word에 순서대로 저장
for key in a_dict:
    while a_dict[key]>1:
        word += key
        a_dict[key] -= 2    # 알파벳은 대칭으로 등장하기 때문에 개수를 2씩 줄임

# 중앙에 올 알파벳을 odd_alphabet에 저장
for key in a_dict:
    if a_dict[key] == 1:
        odd_alphabet = key
        odd += 1

if odd>1:   # odd_alphabet이 1개 이상인 경우
    print("I'm Sorry Hansoo")
else:
    print(word + odd_alphabet + word[::-1])
