T = int(input())

for test_case in range(1, T + 1):
    #입력 받음
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    #오름차순 정렬
    w.sort()
    t.sort()
    
    result = 0
    for _ in range(min(N, M)):
        if w[-1] > t[-1]: # 화물을 옮길 차가 없으면
            w.pop() # 화물 버림
        else: # 무거운 화물부터 적재용량 높은 트럭에 적재
            result += w.pop()
            t.pop()
            
    print('#{} {}'.format(test_case, result))