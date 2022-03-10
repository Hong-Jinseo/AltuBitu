#백준 10804
#카드 역배치

N = 10 #주어진 구간의 개수
card = [i for i in range(1, 21)] #1번부터 20번까지 카드 리스트에 저장

for _ in range(N):
    a, b = map(int, input().split())
    card[a-1:b] = reversed(card[a-1:b])

for i in card:
    print(i, end=' ') #' '로 출력 값들 이어주기