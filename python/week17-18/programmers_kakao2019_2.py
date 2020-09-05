def solution(food_times, k):
    answer = 0

    next = {}
    for i in range(len(food_times)):
        if i == len(food_times)-1:
            next[i] = 0
        else:
            next[i] = i+1

    bfrIdx = len(food_times)-1
    idx = 0

    while k != 0:
        food_times[idx] -= 1
        if food_times[idx] == 0:
            if bfrIdx == idx:
                return -1
            next[bfrIdx] = next[idx]
            del next[idx]
            idx = next[bfrIdx]
        else:
            bfrIdx = idx
            idx = next[idx]
        k -= 1

    return idx + 1


def main():
    answer = solution([1, 1], 2)
    print(answer)

if __name__ == '__main__':
    main()

## NEXT 로 해싱해서 넘기려고 했으나, 효율성 테스트에서 실패ㅠㅜ
