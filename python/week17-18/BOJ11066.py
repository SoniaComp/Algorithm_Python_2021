import sys
MAX = sys.maxsize

def solution(n, data):
    dp = [[0]*n for _ in range(n)] # i부터 j까지의 합의 최소
    sum_data = [0] # 인접한 두행의 합을 빨리 구해보자!
    for d in data:
      sum_data.append(sum_data[-1]+d) # 처음부터 ~ idx 번째까지의 합

    for idx in range(1, n):
      for i in range(n-idx):
        j = idx + i
        dp[i][j] = MAX
        for k in range(i, j): 
          # dp[i][j]는 어떤 걸까...
          dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+sum_data[j+1]-sum_data[i]) # 부분정복으로 계속 최소를 구해나간다.
    
    return dp[0][n-1]

# sum_data를 구하는 이유: 최소 연쇄 행렬 곱셈
# 두 개 이상의 행렬을 곱할 때, 최소 곱셈 횟수를 구하는 문제

def main():
    stdin = sys.stdin
    T = int(stdin.readline().strip())
    for i in range(T):
        K = int(stdin.readline().strip())
        data = [int(x) for x in stdin.readline().split()]
        print(solution(K, data))


if __name__ == '__main__':
    main()

# 처음 시도한 방법
# 맨 앞 2개씩 이렇게 작은 순서대로
'''
while(1):
    data_size = len(data)
    if data_size == 1:
        break
    for i in range(data_size//2):
        sum_cost = data[2*i]+data[2*i+1]
        ans += sum_cost
        sum_data.append(sum_cost)
    if data_size % 2 == 1:
        sum_data.append(data[data_size-1])
    data = sum_data
    sum_data = []
'''
# 예상 가능한 예외 상황
# 1을 80번 더하는게 98 한번 더 하는 것보다 값이 적다.
# 동적 계획법: 주어진 문제를 여러 하위 문제로 나눠서 푸는 것
'''
가능한 모든 경우의 수
1,2,3,4
1, min((2,3), 3 | 2, (3,4)) / (1,2), (3,4) / min((1,2), 3|1, (2,3)), 4 
-> O(n^3)의 시간 복잡도
'''
# Knuth 최적화: 동적 계획법으로 해결하는 문제에서 시간 복잡도를 O(n^3)에서 O(n^2)까지 줄일 수 있는 강력한 알고리즘
'''
이차원 배열인 C와 C를 이용한 Dynamic Programming을 적용한 이차원 배열 DP가 있다고 했을 때
1.점화식의 형태: DP[i][j] = main(DP[i][k]+DP[k][j])+C[i][j]
2.사각부등식: C[a][c]+C[b][d] <= C[a][d]+C[b][c]
3.단조성: C[b][c]<=C[a][d]
'''