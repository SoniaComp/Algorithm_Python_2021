# 색종이
# →⌟↑ 이런식으로 돌면서 체크
# 시간 10개의 줄: 10 * 10 * 10 * 10 < 1초

# checkpoint
# 큰 상자에 포함될 수록 절약된다.
import sys

'''
# →⌟↑ 
dr = [(0, 1), (1, 0), (0, -1)]
def scan_sq(current, space, visited):
    cx, cy = current
    # SCAN →⌟↑ 
    #####
    # 스택에 방문한 데 넣어놓고, 방문하면서 visited 보다 크면 넣기
    #####
def stick_sq(current, space, visited):
    cx, cy = current
    # visited에서 숫자가 큰 것부터 붙여넣기
'''

# 그냥 아예 처음부터 큰 거 붙이기


def stick_sq(current, size, space, sticked):
    cx, cy = current
    square = True
    visited = []
    for i in range(size): # 아래 세줄을 파이썬 하게 바꾼다면?
        for j in range(size):
            x, y = (cx+i, cy+j)
            if sticked[x][y] == 0 and space[x][y] == 0:
                square = False
                break
            visited.append((x, y))
    if sqaure = False:
        return space, sticked, 0 # 계속해서 공간값을 넘겨주는게 좋은 걸까?
    else:
        while visited:
            x, y = visited.pop()
            sticked[x][y] == 1
    return space, sticked, 1


def solution(square):
    size = len(square)
    space = square # 궁금증.. 값 변경해주기 위해서 이렇게!?!? iterator!?
    ans = 0
    sticked = [[0]*size for _ in range(size)]

    # for s in reversed(range(size + 1)) # 이것보다 직관적인 것 같아서..
    for s in range(size, 0, -1):  # 언어에 대한 궁금증.. 왜 마지막 값은 포함 안 될까?
        # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        # 0, 0~1, 0~2, 0~3, 0~4
        for x in range(s+1):
            for y in range(s+1):
                space, visited, ans_add = stick_sq((x, y), size, square, visited)
                ans += ans_add
    return ans


def main():
    stdin = sys.stdin
    square = [map(int, stdin.readline().split()) for _ in range(10)]
    solution(square)


if __name__ == "__main__":
    main()

'''testcase
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

0

0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

4

0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

5

0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

-1

0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 1 1 1 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

7

1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1

4

0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 1 1 1 1 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1

6

0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 0 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 1 1 0 0 0
0 1 1 1 0 0 0 0 0 1

5
'''
