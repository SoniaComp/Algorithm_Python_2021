def solution(A):
    A_LEN = len(A)
    if A_LEN == 0:
        return -1
        
    dominator = sorted(A)[A_LEN // 2]
    return A.index(dominator) if A.count(dominator) > A_LEN/2 else -1