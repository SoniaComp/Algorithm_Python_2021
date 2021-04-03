from collections import Counter
def solution(N, stages):
    answer = [] # (stage, 실패율)
    c = Counter(stages)
    all_num = len(stages)
    try_num = all_num
    for i in range(1, N+1):
        if try_num <= 0:
            answer.append((i, 0))
            continue
        answer.append((i, c[i]/try_num))
        try_num = try_num - c[i]
    return list(map(lambda x: x[0], sorted(answer, key=lambda x: x[1], reverse=True)))