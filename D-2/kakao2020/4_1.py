def solution(n, build_frame):
    answer = []
    pillar = [([1] + [0]*(n)) for _ in range(n+1)] # 바닥은 기둥을 세울 수 있으니까
    roof = [[0]*(n+1) for _ in range(n+1)]
    
    # 구조물 놓기
    def roof_possible(x, y):
        return pillar[x][y] or pillar[x+1][y] or (roof[x][y] and roof[x+1][y])
    
    for x, y, obj, cmd in build_frame:
        if cmd:
            if obj == 0 and (pillar[x][y] or roof[x][y]):
                pillar[x][y+1] += 1
            elif obj == 1 and roof_possible(x, y):
                roof[x][y] += 1
                roof[x+1][y] += 1
        elif obj == 0:
            pillar[x][y+1] -= 1
        elif obj == 1:
            roof[x][y] -= 1
            roof[x+1][y] -= 1
    pillar_set = [(x, y-1, 0) for x in range(n+1) for y in range(n+1) if (y!= 0 and pillar[x][y])]
    roof_set = [(x, y, 1) for x in range(n+1) for y in range(n+1) if roof[x][y] and (x<n and roof[x+1][y])]
    answer = sorted(pillar_set+roof_set, key = lambda x: (x[0], x[1]))
    
    return answer