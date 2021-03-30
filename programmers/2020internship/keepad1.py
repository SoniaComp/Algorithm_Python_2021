def solution(numbers, hand):
    answer = []
    l_pos = r_pos = 0
    hand = 'L' if hand == 'left' else 'R'
    for num in numbers:
        if num % 3 == 1 :
            l_pos = num
            answer.append('L')
        elif num % 3 == 0:
            r_pos = num
            answer.append('R')
        elif abs(r_pos - num) < abs(l_pos - num):
            r_pos = num
            answer.append('R')
        elif abs(r_pos - num) > abs(l_pos - num):
            l_pos = num
            answer.append('L')
        else:
            answer.append(hand)
            if hand == 'L':
                l_pos = num
            else:
                r_pos = num
    return ''.join(answer)