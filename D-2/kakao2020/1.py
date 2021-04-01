def solution(s):
    min_len = float('inf')
    
    # 예외처리 절대해주어야 함!!
    if len(s)==1:
        return 1
    
    for slice_len in range(1,len(s)):
        prev_index = 0
        index = slice_len
        answer = ''
        count = 1
        while True:
            next_index = index + slice_len
            if s[prev_index: index] == s[index: next_index]:
                count += 1
            else:
                answer += str(count) + s[prev_index: index] if count !=1 else s[prev_index: index]
                count = 1
            prev_index, index = index, next_index
            if index > len(s) and count == 1:
                answer += s[prev_index:]
                break
        min_len = min(min_len, len(answer))
    return min_len