T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    sum_now = sum(num_list[0:M])
    sum_max = sum_min = sum_now
    for i in range(M, len(num_list)):
            sum_now = sum_now + num_list[i] - num_list[i-M]
            if sum_now > sum_max:
                sum_max = sum_now
            if sum_now < sum_min:
                sum_min = sum_now
    print('#{} {}'.format(test_case, sum_max-sum_min))
    # ///////////////////////////////////////////////////////////////////////////////////
