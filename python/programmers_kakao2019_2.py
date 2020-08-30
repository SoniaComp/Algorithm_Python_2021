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

## 라인 프로파일러로 성능을 분석하신다는 데이터분석 일을 하시는 스터디원분 코드로 돌려보니
# 내가 4.87ms -> 0.50ms
# 42.02ms -> 0.80ms
## 사용 메모리가 비슷한데, 어떻게 이렇게 큰 차이가 나는 걸까?