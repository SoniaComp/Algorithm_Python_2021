'''
2 / 3 / 5 / 7
50 33 20 14
117

2,3 / 2,5 / 2,7 / 3,5 / 3,7 / 5,7
16 10 7 6 4 2
72

2,3,5 / 2,5,7 / 2,3,7 / 3,5,7
3 1 2 
'''
# 백트래킹
# https://medium.com/@jeongdowon/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-backtracking-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-13492b18bfa1
# 백트래킹(backtracking)이란? : 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법을 말합니다. 최적화 문제와 결정 문제를 푸는 방법이 됩니다.
# https://chanhuiseok.github.io/posts/algo-23/

import sys
from itertools import combinations
from operator import mul
from functools import reduce

# 집합 관계
# 파이썬 reduce 관계


def solution(prime_nums, N, M):
    ans = 0
    '''
    for i in prime_nums:
        ans += M // i
    for i in list(combinations(prime_nums, 2)):
        ans -= M // (i[0]*i[1])
    for i in list(combinations(prime_nums, 3)):
        ans += M // (i[0]*i[1]*i[2]) 
    '''
    for i in range(1, N+1):
        flag = (-1) ** (i+1)
        for j in combinations(prime_nums, i):
            ans += M // reduce(mul, j) * flag
    return ans


def main():
    stdin = sys.stdin
    N, M = map(int, stdin.readline().split())
    prime_nums = list(map(int, stdin.readline().split()))
    print(solution(prime_nums, N, M))


if __name__ == '__main__':
    main()
