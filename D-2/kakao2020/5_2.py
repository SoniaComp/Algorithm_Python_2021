# 정확도 68%
def solution(n, weak, dist):
    MAX_QSIZE = n
    if len(weak) == 1:
        return 1
    
    wall = [False] * MAX_QSIZE
    
    for w in weak:
        wall[w] = True # 취약점
    answer = 0
    for d in reversed(dist):
        if not weak:
            return answer
        check = [] # start, check_num
        for w in weak:
            idx = start = w
            check_num = 1
            for _ in range(d):
                if idx == MAX_QSIZE-1:
                    idx = 0
                else:
                    idx += 1
                if wall[idx]:
                    check_num += 1
            check.append((start, check_num))
        check = sorted(check, key=lambda x: x[1])
        
        idx = best_start = check[-1][0]
        weak.remove(idx)
        wall[idx] = False
        for _ in range(d):
            if idx == MAX_QSIZE-1:
                idx = 0
            else:
                idx += 1
            if wall[idx]:
                weak.remove(idx)
                wall[idx] = False
        answer += 1
    if not weak:
        return answer  
    return -1