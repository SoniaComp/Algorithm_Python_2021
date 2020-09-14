import sys
'''
9 1 1 
9 1 1 2 5 4 2 6
9 7 6 2 5 9 9 9

1 1 3
1 2 3 4 0 
1 2 3 4 4 0
1 2 3 4 5
9 8 3 4 6
'''
# string으로 해도 됨
# val.startswith(pre_num) : prefix인지만 해결하면 됨
# 예외처리

def solution(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            for j in range(len(nums[i])):
                if nums[i][j] != nums[i+1][j]:
                    break
                if j == len(nums[i])-1:
                    return 0
    return 1


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        # map(int, sys.stdin~) 하면 map 객체를 반환하기 때문에 list()를 씌워준다.
        nums = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
        print("YES" if solution(nums) else "NO")


if __name__ == '__main__':
    main()
