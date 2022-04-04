import sys
input = sys.stdin.readline

"""
 가지치기 효율: 80ms
 9X9의 스도쿠에서 각 행, 열, 3x3 사각형에 1~9가 존재하는지 체크하는 2차원 배열 활용
 각 2차원 배열의 행: 어느 부분에 대한 체크인지(행, 열, 3x3), 0번 인덱스부터 시작
 각 2차원 배열의 열: 1 ~ 9 숫자 체크
 행과 열은 바로 사용하면 됨
 (ex) check_row[3][2] = true;  //3행에 2라는 숫자가 존재한다는 것
      check_col[8][9] = false; //8열에 9라는 숫자가 존재하지 않는다는 것
 3x3 사각형 (하나를 각 구역이라고 표현)
 -> 행을 3으로 나눈 몫과 열을 3으로 나눈 몫으로 구역 0부터 8까지 다음과 같이 나타낼 수 있음
 (0,0) (0,1) (0,2)
 (1,0) (1,1) (1,2)
 (2,0) (2,1) (2,2)
 -> 1차원 배열 인덱스로 구분하기 위해 각 (행 / 3)값에 3을 곱한 후 (열 / 3)을 더함
 -> 따라서 3x3 사각형의 구간은 (row / 3) * 3 + (col / 3) = 0 ~ 8인 구간으로 나눌 수 있음
"""

SIZE = 9    # 스도쿠 한 행 사이즈
check_row = [[False] * (SIZE + 1) for _ in range(SIZE)]     # 각 행의 숫자 존재 여부 체크
check_col = [[False] * (SIZE + 1) for _ in range(SIZE)]     # 각 열의 숫자 존재 여부 체크
check_3x3 = [[False] * (SIZE + 1) for _ in range(SIZE)]     # 각 3x3 사각형의 숫자 존재 여부 체크

def calc_area(x, y):                # x,y가 스도쿠 내 몇 번쨰 3x3 사각형에 있는지 반환
    return (x // 3) * 3 + y // 3    # 왼쪽에서 오른쪽, 위에서 아래 순서로 0~8

def fill_sudoku(cnt):               # 스도쿠를 채우는 메소드
    if cnt == SIZE * SIZE:          # 스도쿠가 다 채워졌다면 (cnt가 스도쿠 칸의 총 개수와 일치한다면)
        return True                 # 종료
    
    x, y = cnt // SIZE, cnt % SIZE  # x, y에 (0,0), (0,1), ... , (0,8), (1,0), (1,1) 순서로 할당

    if sudoku[x][y] > 0:    # 이미 숫자가 채워진 칸이라면 다음 칸으로 넘어감
        return fill_sudoku(cnt + 1) # 매개변수에 1을 더해 자기자신 재호출

    for i in range(1, SIZE + 1):    # 1~9까지 넣어보기
        if check_row[x][i] or check_col[y][i] or check_3x3[calc_area(x, y)][i]: # i가 동일 행, 열, 3x3 사각형 내에 있다면
            continue                # 반복문 처음으로 돌아감

        check_row[x][i] = True                  # x행에 해당 숫자(i)가 있음을 기록
        check_col[y][i] = True                  # y열에 해당 숫자(i)가 있음을 기록
        check_3x3[calc_area(x, y)][i] = True    # x,y가 속한 3x3 칸에 해당 숫자(i)가 있음을 기록
        sudoku[x][y] = i                        # 스도쿠 x, y 위치에 i 기록

        if fill_sudoku(cnt + 1):    # 스도쿠가 다 채워졌다면
            return True             # 종료

        # 초기화 (스도쿠가 다 채워지지 않았기 때문)
        check_row[x][i] = False     # x행에 i가 있다는 기록 삭제
        check_col[y][i] = False     # y열에 i가 있다는 기록 삭제
        check_3x3[calc_area(x, y)][i] = False   # 3x3칸에 i가 있다는 기록 삭제
        sudoku[x][y] = 0            # 스도쿠 x,y 위치가 비어있다고 수정

    return False                    # 위의 retrun True에서 걸리지 않았다면 False 반환

# 입력
sudoku = [list(map(int, input().split())) for _ in range(SIZE)] # input을 '스도쿠 한 행 크기'만큼 반복해서 받음

# 스도쿠 상태 표시
for i in range(SIZE):               # i: 스도쿠의 행
    for j in range(SIZE):           # j: 스도쿠의 열
        if sudoku[i][j] == 0:       # i행 j열의 값이 0이라면
            continue                # 반복문 처음으로 돌아감 (j+=1)
        check_row[i][sudoku[i][j]] = True                   # i행에 해당 숫자(sudoku[i][j])가 있음을 기록
        check_col[j][sudoku[i][j]] = True                   # j열에 해당 숫자(sudoku[i][j])가 있음을 기록
        check_3x3[calc_area(i, j)][sudoku[i][j]] = True     # 3x3칸에 해당 숫자(sudoku[i][j])가 있음을 기록

# 연산
fill_sudoku(0)      # 스도쿠 채우는 백트래킹 함수 호출

# 출력
for line in sudoku: # 스도쿠 리스트에 순서대로 접근
    print(*line)    # *list -> 리스트의 요소를 하나씩 풀어서 print()에 인자로 넣어줌
                    # print(*[1, 2, 3]) == print(1, 2, 3)