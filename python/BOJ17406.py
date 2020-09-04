from itertools import permutations
import sys
import copy
max_size = sys.maxsize


def min_sum(arr, N, M):
    ans = max_size
    for i in range(1, N+1):
        sum = 0
        for j in range(1, M+1):
            sum += arr[i][j]
            arr[i][j]
        if sum < ans:
            ans = sum
    return ans


def rotate_arr(arr, params):
    stdin = sys.stdin
    r, c, s = params

    for i in range(1, s+1):
        tmp = arr[r-i][c-i]
        for j in range(0, 2*i):
            arr[r-i+j][c-i] = arr[r-i+j+1][c-i]
        for j in range(0, 2*i):
            arr[r+i][c-i+j] = arr[r+i][c-i+j+1]
        for j in range(0, 2*i):
            arr[r+i-j][c+i] = arr[r+i-j-1][c+i]
        for j in range(0, 2*i):
            arr[r-i][c+i-j] = arr[r-i][c+i-j-1]
        arr[r-i][c-i+1] = tmp
    return arr


def solution(arr, N, M, params_arr):
    for params in params_arr:
        arr = rotate_arr(arr, params)
    return min_sum(arr, N, M)


def main():
    stdin = sys.stdin
    N, M, K = map(int, stdin.readline().split())
    arr = [[0]*(M+1)] + [[0]+list(map(int, stdin.readline().split()))
                         for _ in range(N)]
    rotate_params = [list(map(int, stdin.readline().split()))
                     for _ in range(2)]
    rotate_params_list = list(permutations(rotate_params))

    ans = max_size
    for rotate_params_order in rotate_params_list:
        new_arr = copy.deepcopy(arr)
        arr_min = solution(new_arr, N, M, rotate_params_order)
        if arr_min < ans:
            ans = arr_min

    print(ans)


if __name__ == '__main__':
    main()
