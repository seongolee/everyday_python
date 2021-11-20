"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다. 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
"""


def test_check():
    print('test')
    exit



# 비교할 기준 설정
BW = [0 for _ in range(8)]
WB = [0 for _ in range(8)]
result = 12345

for i in range(8):
    if i % 2 == 0:
        BW[i] = list(map(str, "BWBWBWBW"))
        WB[i] = "W B W B W B W B".split()
    else:
        BW[i] = "W B W B W B W B".split()
        WB[i] = "B W B W B W B W".split()


# 행과 열이 시작되는 값을 파라미터로 받아서 count값을 int형으로 반환
def BW_cnt(x, y: int) -> int:
    cnt = 0

    for i in range(8):
        for j in range(8):
            if chess_board[x + i][y + j] != BW[i][j]:
                cnt += 1

    return cnt

def WB_cnt(x, y: int) -> int:
    cnt = 0

    for i in range(8):
        for j in range(8):
            if chess_board[x + i][y + j] != WB[i][j]:
                cnt += 1

    return cnt

# N = 가로, M = 세로, B = black, W = white
N, M = map(int, input("행 열 입력> ").split())
# if N < 8 or M < 8:
#     N, M = map(int, input("다시 입력해주세요, 행 열 입력(8 8이상)> ").split())

# 행을 만들만큼의 1차원 리스트를 만들고, range(N)만큼 만들어진 리스트에 0부터 N-1까지 열값을 넣으면 2차원 배열을 만들 수 있다.
chess_board = [0 for _ in range(N)]

for i in range(N):
    # 한줄의 입력값이 행길이와 같은지 확인
    check_M = input()
    if len(check_M) != M:
        while True:
            check_M = input(f"{M}글자르 다시 입력해주세요> ")
            chess_board[i] = list(map(str, check_M))
            if len(check_M) == M:
                break

    else:
        chess_board[i] = list(map(str, check_M))

for i in range(i + 8):
    if i > N:
        break
    for j in range(j + 8):
        if j > M:
            break
        tmp = min(WB_cnt(i, j), BW_cnt(i, j))

        if tmp < result:
            result = tmp

print(result)