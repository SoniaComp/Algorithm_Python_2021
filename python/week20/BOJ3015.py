'''
옛날에 카카오 코딩테스트에서 봤던 것 같다.
      2 4 1 2 2 5 1
7:    o o 4 4 4 o 5
2:      o 4 4 4 4 4
4:        o o o o 5
1:          o 2 2 2
2:            o o 5
2:              o 5
5:                o

시각화 해보면
2: o o        1
4: o o o o    1
1: o          3
2: o o        3
2: o o        1
5: o o o o o  0


N <= 500,000이기 때문에, N^2 시간 복잡도로 풀면 1초안에 풀지 못한다.
키의 값도 2^31 이니까 10^9정도 되니까
파이썬은 오버플로우가 없다고 하더라도, int

'''
import sys


# 우선 N^2 복잡도로 풀어본다.
def solution(N, arr):
    ans = 0
    for idx in range(N-1):
        if arr[idx] < arr[idx+1]:
            ans += 1
            continue
        count = 1
        max_height = arr[idx+1]
        for i in range(2, N-idx):
            if arr[idx+i] >= max_height:
                count += 1
                max_height = arr[idx+i]
                if arr[idx] < max_height:
                    break
        ans += count
    return ans


def main():
    stdin = sys.stdin
    N = int(input())
    arr = list(int(input()) for _ in range(N))
    print(solution(N, arr))


if __name__ == "__main__":
    main()
