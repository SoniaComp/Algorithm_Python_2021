def solution(A):
    # write your code in Python 3.6

    lower_list = []
    upper_list = []
    for i, a_elm in enumerate(A):
        lower_list.append(i - a_elm)
        upper_list.append(i + a_elm)

    lower_list.sort()
    upper_list.sort()
    j = 0
    counter = 0
    total_len = len(A)
    for i in range(total_len):
        while(j < total_len and lower_list[j] <= upper_list[i]): # if문 조건 순서도 중요하네..
            # 0 인 경우는 1개 따져줘야되니 +1했다가 어차피 자기 자신은 제외(-1)하니까 그러려니하는 걸로
            counter += j + 1 - 1  # 중복 아님
            counter -= i # 이미 upper의 index로 세어버린 원들의 개수는 빼버림 # 중복 제거
            j = j + 1

            if counter > 10000000:
                return -1

    return counter