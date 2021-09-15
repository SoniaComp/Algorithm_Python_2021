def solution(X, A):
    leafs = [(num, i) for i, num in enumerate(A)]
    leafs = sorted(leafs)
    cur_num = 0
    max_num = 0
    for leaf in leafs:
        num, i = leaf[0], leaf[1]
        if num - cur_num > 1:
            return -1
        if num - cur_num == 0:
            continue
        elif num - cur_num == 1:
            max_num = max(max_num, i)
            cur_num = num
        if num == X:
            return max_num
    return -1