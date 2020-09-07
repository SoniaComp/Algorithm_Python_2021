# 문제분석
# 비트 연산으로 벽에 대한 정보를 체크한다.
#
import sys

# 비트연산해서 하나라도 뚫려 있으면 그리로 갈 수 있음
# 왼, 북, 오, 남
directions = [0b0001, 0b0010, 0b0100, 0b1000]

# 여기서는 이걸 만들려고 함..
# [[인접한 방의 수], []]
# 1차원: 방의 갯수
# 2차원: 해당 방에 인접한 방의 수

def bfs(castle, check, start):
    queue = [start]
    while queue:
        count = 0
        x, y = queue.pop()
        if check[x][y]:
            continue
        check[x][y] = 1
        count += 1
        now = bin(castle[x][y])
        for i in directions:
            if bin(directions[i] & now):
                if i == 0:
                    queue.append((x-1, y))
                    break
                elif i == 1:
                    queue.append((x, y-1))
                    break
                elif i == 2:
                    queue.append((x+1, y))
                    break
                else:
                    queue.append((x, y+1))
    return count


def solution(castle, m, n):
    # 비트연산해서 하나라도 뚫려 있으면 그리로 갈 수 있음
    directions = [0b0001, 0b0010, 0b0100, 0b1000]

    # 여기서는 이걸 만들려고 함.. room
    # [[인접한 방의 수], []]
    # 1차원: 방의 갯수
    # 2차원: 해당 방에 인접한 방의 수
    check = [[0 for i in range(m)] for j in range(n)]
    room = []
    count = []

    for i in range(m):
        for j in range(n):
            if check[i][j] is 0:
                cnt = bfs(castle, check, (i, j))
                count.append[cnt]
    print(len(count))
    print(max(enumerate(count)))


def main():
    stdin = sys.stdin
    m, n = map(int, stdin.readline().split())
    castle = [map(int, stdin.readline().split()) for i in range(n)]
    solution(castle, n, m)


if __name__ == '__main__':
    main()
