nums = [i for i in range(1,4)]  # 1~3 리스트

# 부분집합 리스트 구하기
lst = [] 
for i in range(1 << len(nums)):  # 경우의 수 :  2^len(nums)
    sub_lst = []  # 부분집합
    for j in range(len(nums)):
        print('-')
        print(i)
        print(1<<j)
        if i & (1 << j):  # 부분집합 만들기
            sub_lst.append(nums[j]) # 포함되는 원소 추가
    print(sub_lst)
    print('---------')
    lst.append(sub_lst)  # 리스트에 부분집합 추가
    print(lst)
    
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    
    for m in lst:  # 모든 부분집합 중
        if len(m) == N and sum(m) == K:  # 길이 N, 합 K 일 때
            result += 1
    
    print('#{} {}'.format(test_case, result))