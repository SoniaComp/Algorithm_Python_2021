# DP를 이용한 최적화 문제를 해결하는 알고리즘 설계 절차
'''
1) 문제의 입력에 대해서 '최적'의 해답을 주는 재귀적 속성(recursive property)을 설정
2) 상황적으로 최적의 해답을 계산
-> ex) 플로이드 알고리즘에서, D, P 계산
3) 최적화
-> ex) 플로이드 알고리즘에서 경로 출력

A. 플로이드-와샬 알고리즘:https://www.youtube.com/watch?v=9574GHxCbKc
모든 정점에서 모든 정점으로의 최단 경로
다익스트라는 가장 적은 비용을 하나씩 꺼내서 선택했다면, 
플로이드 와샬은 ""거쳐가는 정점""을 기준으로 한다. -> 애초에 거쳐가는 노드를 다 확인하기

-> 현재까지 계산된 최소비용
--> 반복해서 모든 최소 비용을 구하는 것
--> 반복: 거쳐가능 정점이 기준(가장 적은)
--> 노드 1을 거치는 경우, 노드 2를 거치는 경우...

B. 크누스 알고리즘:https://blog.myungwoo.kr/98
Dynamic Programming에서 점화식이 특정 조건을 만족할 때 활용할 수 있는 최적화 기법
1) 조건: DP 점화식 꼴
D[i][j] = min i<k<j(D[i][k]+D[k][j])+C[i][j]
2) 조건: 사각 부등식(Quadrangle Inequality)
C[a][c]+C[b][d]<=C[a][d]+C[b][c], a<=b<=c<=d
3) 조건: 단조성(Monotonicity)
C[b][c]<=C[a][d], a<=b<=c<=d

* 이중리스트로 구성할 경우, 조건 3 만족
* 조건 2과 조건 3을 만족하면 조건 1의 형태의 점화식을 이용해서 문제를 풀 수 있다.


-> i~k 까지 더한 비용의 최솟값 + k+1~j까지 더한 비용의 최솟값
-> subproblem으로 나눠서 생각할 수 있다.
-> 대각선 방향으로 값을 채워준다.

'''

import sys
MAX = sys.maxsize


def solution(K, data):
    table = [[0]*K for _ in range(K)]

    for i in range(K-1):
        table[i][i+1] = data[i] + data[i+1]
        for j in range(i+2, K):
            table[i][j] = table[i][j-1] + data[j]

    for d in range(2, K):
        for i in range(K-d):
            j = i+d
            minimum = [table[i][K]+table[K+1][j] for K in range(i, j)]
            table[i][j] += min(minimum)

    return table[0][K-1]


def main():
    stdin = sys.stdin
    T = int(stdin.readline().strip())
    for i in range(T):
        K = int(stdin.readline().strip())
        data = [int(x) for x in stdin.readline().split()]
        print(solution(K, data))


if __name__ == '__main__':
    main()

# 크누스.. 사실 이해하려고 노력중이다. 