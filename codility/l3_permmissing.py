def solution(A):
    s = sum(A)
    s_sum = sum(range(len(A)+2))
    return s_sum - s