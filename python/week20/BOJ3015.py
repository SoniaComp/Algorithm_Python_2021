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
import collections

# 우선 N^2 복잡도로 풀어본다.
# def solution(N, arr):
#     ans = 0
#     for idx in range(N-1):
#         if arr[idx] < arr[idx+1]:
#             ans += 1
#             continue
#         count = 1
#         max_height = arr[idx+1]
#         for i in range(2, N-idx):
#             if arr[idx+i] >= max_height:
#                 count += 1
#                 max_height = arr[idx+i]
#                 if arr[idx] < max_height:
#                     break
#         ans += count
#     return ans

def solution(N, arr):
    stack = [] # [키, 연속 몇명]
    ans = 0
    for i in range(N):
        height = arr[i]
        # 현재 사람의 키가 스택의 top에 있는 사람보다 크다면,
        # 현재 사람 이후 쌍을 이루지 못함
        while stack and stack[-1][0] < height:
            ans += stack[-1][1]
            del stack[-1]
        
        # 맨앞에 사람을 세움
        if not stack:
            stack.append([height, 1])
        else:
            # 같은 키의 경우 따로 처리
            if stack[-1][0] == height:
                cur = stack[-1]
                del stack[-1]
                ans += cur[1]
                
                # 스택 내 제일 큰 사람과 쌍을 이룸
                if stack:
                    ans += 1
                
                # 연속해서 같은 키가 나옴
                cur[1] += 1
                stack.append(cur)
            
            # 더 작은 사람
            stack.append([height, 1])
            ans +=1

    return ans


def main():
    stdin = sys.stdin
    N = int(input())
    arr = list(int(input()) for _ in range(N))
    print(solution(N, arr))


if __name__ == "__main__":
    main()
