from collections import deque
def solution(board, moves):
    board = list(map(list, list(zip(*board[::-1]))))
    basket = []
    cnt = 0
    for move in moves:
        cur_b = board[move-1]
        if not cur_b:
            continue
        cur = None
        while cur_b:
            cur = cur_b.pop()
            if cur:
                break
        if not cur:
            continue
        if basket and basket[-1] == cur:
            cnt += 2
            basket.pop()
        else:
            basket.append(cur)
    return cnt