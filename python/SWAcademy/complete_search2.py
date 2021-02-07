def DFS(Current):
    global my_min, my_sum

    if my_sum < my_min:
        visited[Current] = True

        if False not in visited: # 사무실로 돌아오기
            my_sum += my_map[Current][0]
            if my_sum < my_min: # 최소값이면
                my_min = my_sum # 갱신
            my_sum -= my_map[Current][0]
        else: # 방문하지 않은 곳
            for Next in range(N):
                if visited[Next] == False:
                    my_sum += my_map[Current][Next]
                    DFS(Next)
                    my_sum -= my_map[Current][Next]

        visited[Current] = False
    

T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    my_min = 1000
    my_sum = 0
    DFS(0)
    print('#{} {}'.format(test_case, my_min))