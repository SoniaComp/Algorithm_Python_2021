from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
K_list = [list(map(int, input().split())) for _ in range(K)]

result = float('inf')

for perm in permutations(K_list):
    my_map = deepcopy(A)
    for r, c, s in perm:
        for rad in range(1, 1+s):
            # 시작점
            y, x = r-1-rad, c-1-rad
            temp = my_map[y][x]
            # 돌리기
            for _ in range(2*rad):
                x += 1
                my_map[y][x], temp = temp, my_map
            for _ in range(2*rad):
                y += 1
                my_map[y][x], temp = temp, my_map[y][x]
            for _ in range(2*rad):
                y -= 1
                my_map[y][x], temp = temp, my_map[y][x]

        # 결과 갱신
        for i in range(N):
            sub_res = sum(my_map[i])
            if sub_res < result:
                result = sub_res

    print(result)
'''
float 자료형 양의 무한대, 음의 무한대
maximum = float('inf')
minimum = float('-inf')

int 자료형 정수 최대아 최소값
import sys
maximum = sys.maxint
mininum = sys.minint

sys.maxsize 범위 초과시 long 형으로 자동 변환되나 타입은 int로 표기된다.
maximum = sys.maxsize
minimum = -(sys.maxsize+1)
'''
