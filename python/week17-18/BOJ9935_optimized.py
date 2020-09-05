# 코드의 병목점을 찾아보자.
# line_profiler
# $ pip install line_profiler

# profiling 하고자 하는 함수 앞에 @profile 지시어 붙이기
# kernprof 명령을 사용하여 프로파일링을 라인 단위로 계산

# 개선해야할 코드 부분
# newstring = ''.join(string.split(bomb))
# split의 시간 복잡도: O(NM) - 빅오 표기법 정확하진 않음.. 공부해야 할 듯
# join의 복잡도: O(N) - 빅오 표기법 정확하진 않음.. 공부해야 할 듯
# 스택을 이용한 축적 & 리스트 비교

# 참고 블로그: https://ksshlee.github.io/baekjoon/%EB%B0%B1%EC%A4%80-9935-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AD%EB%B0%9C/
# 리스트 비교
'''
for j in range(-1, (-len(bomb))-1, -1):
  if ans[j] != bomb[j]:
    ...
'''
# 꼭 index 0 부터 비교할 필요는 없다.

import sys


@profile
def solution(text, bomb):  # BigO로 얼마나 효율적이 됐을까
    ans = []  # 문자열을 넣을 스택

    for i in text:
        # 하나씩 스택에 넣어준다.
        ans.append(i)
        if len(ans) >= len(bomb):
            # 뒤에서부터 검사.. 왜냐하면 앞에서부터 하면 112ab이고 12ab 일치하지 않음
            check = []
            checkcount = 0
            same = True
            for j in range(-1, (-len(bomb))-1, -1): # 여기서 가장 많은 시간
                if ans[j] != bomb[j]:
                    # 하나라도 다르면 false
                    same = False
                    break

            if same == True:
                a = 0
                # bomb의 길이만큼 pop
                while a < len(bomb):
                    ans.pop()
                    a += 1

    # 길이가 0이면 FRULA
    if len(ans) == 0:
        return "FRULA"
    else:
        return ''.join(ans)


def main():
    stdin = sys.stdin
    string = stdin.readline().strip()
    bomb = stdin.readline().strip()
    print(solution(string, bomb))


if __name__ == '__main__':
    main()
