"""
플레이어가 1~100 중에서 임의의 수를 정하면, 컴퓨터가 해당 수를 맞히는 게임입니다.
플레이어가 정한 수가 컴퓨터가 말한 수보다 작으면 플레이어는 '업' 이라고 말하고, 크다면 플레이어는 '다운' 이라고 말해서 힌트를 줍니다.
컴퓨터는 플레이어가 주는 힌트를 토대로, 수를 맞힐 때까지 계속해서 시도합니다.


**[상세설명]**

1. 플레이어가 input 함수를 통해서 1~100 중 임의의 수(P)를 입력한다. (1~100 이외의 수를 입력할 경우, 다시 입력하도록 할 것)
2. 컴퓨터는 플레이어가 정한 수(P)를 가장 빨리 맞힐 수 있도록 수(C)를 말한다. (randrange는 사용하지 말 것)
3. 플레이어는 C와 P를 비교하여, 업 / 다운 중 하나를 입력한다. (직접 '업' 혹은 '다운'을 input 함수를 통해 입력하도록 할 것,
그 이외의 단어를 입력할 경우 다시 입력하도록 할 것, P가 C보다 더 큰데도 플레이어가 거짓말로 '다운'이라고 할 경우에도 다시 입력하도록 할 것)

업: 플레이어가 정한 임의의 수(P)가 컴퓨터가 말한 수(C)보다 높은 경우

다운: 플레이어가 정한 임의의 수(P)가 컴퓨터가 말한 수(C)보다 낮은 경우

1. 2~3번을 컴퓨터가 맞힐 때까지 반복한다. (즉, 2~3번을 while문으로 작성할 것)
2. 컴퓨터가 수를 맞히면 '성공'을 출력한다.
"""
import sys

P = int(input())
P_count = 1
P_count_max = 3
while not (1 <= P <= 100):
    P = int(input(f'다시입력해주세요 ({P_count}/{P_count_max})>'))

    if P_count == P_count_max:
        sys.exit()

    P_count += 1

C_min = 1
C_max = 100
while True:
    C = (C_min + C_max) // 2
    print(C)

    if C < P:
        C_min = C + 1
        C_hint = '업'
    elif C > P:
        C_max = C - 1
        C_hint = '다운'
    else:
        print('성공')
        break

    P_hint = input()

    while not (P_hint == C_hint):
        P_hint = input('다시입력>')
