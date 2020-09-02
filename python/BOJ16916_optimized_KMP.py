'''
전 문제에서 해결했던 스택 문제도 시간 초과로 발생했다.
구글링 하다보니까 라빈 카프 알고리즘을 발견했다.
KMP 알고리즘도.
둘다 O(N*M) 시간 복잡도를 O(N+M)이렇게 선형으로 바꿀 수 있는 아주 멋찐 알고리즘

라빈 카프 알고리즘: https://m.blog.naver.com/PostView.nhn?blogId=ndb796&logNo=221240679247&proxyReferer=https:%2F%2Fwww.google.com%2F
해싱을 기반으로 한 알고리즘
자기 자신의 부분 문자열들끼리 해시 값을 구해놓고 충돌이 일어날 경우, 둘이 같은 문자열인지 비교해서 판정
-> 2의 거듭제곱을 이용해 해시함수를 구하는데
-> 오버플로우가 발생해도, 값자체는 동일해서, 일반적인 CPU(연산장치)의 경우 동일한 간격으로 음의 부호와 양의 부호를 왔다갔다해서, 값이 일치한다.

kmp 알고리즘:https://m.blog.naver.com/PostView.nhn?blogId=ndb796&logNo=221240660061&proxyReferer=https%3A%2F%2Fwww.google.com%2F
접두사와 접미사의 개념을 활용하여 반복되는 연산을 얼마나 줄일 수 있는지를 판별하여, 매칭할 문자열을 빠르게 찾아내어 점프하는 기법
실패할 경우, 점프할 수 있는 실패 테이블을 만드는 것이 포인트(접두사, 접미사 일치를 이용해서)

c++은 빠르당: strstr(대상문자열, 검색할문자열): 문자열을 찾았으면 문자열로 시작하는 문자열의 포인터를 반환, 문자열이 없으면 NULL반환.
'''

import sys

def make_table(pattern):
    pattern_size = len(pattern)
    table = [0 for i in range(pattern_size)]
    j = 0
    for i in range(1, pattern_size):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def solution(txt, subtxt):
    table = make_table(subtxt)

    txt_size = len(txt)
    subtxt_size = len(subtxt)
    j = 0
    
    for i in range(txt_size):
      while j>0 and txt[i] != subtxt[j]:
        j = table[j-1]
      if txt[i] == subtxt[j]:
        if j == subtxt_size-1:
          return 1
        else: 
          j+=1
          
    return 0

def main():
    stdin = sys.stdin
    txt = stdin.readline().strip()
    subtxt = stdin.readline().strip()
    print(solution(txt, subtxt))


if __name__ == '__main__':
    main()
