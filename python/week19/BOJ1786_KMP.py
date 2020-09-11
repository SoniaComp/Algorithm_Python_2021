import sys

'''
Idx 0 1 2 3 4 5 6 7
    a b a c a a b a
-15 0 0 1 0 1 1 0 1
-16 0 0 1 0 0 0 2 3
-17 0 0 1 0 1 1 2 3
'''


def make_table(pattern):
    table = [0] * len(pattern)
    j = 0  # j를 기준으로 패턴 테이블을 채울 건데,
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:  # 다시 초기값이랑 비교해주어야 하니까
            j = table[j-1]  # j를 첫번째로 초기화해줌
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def KMP(T, P):
    result_idx = []
    table = make_table(P)
    j = 0
    for i in range(0, len(T)):
        while j > 0 and T[i] != P[j]:
            j = table[j-1]
        if T[i] == P[j]:
            if j == len(P)-1:
                result_idx.append(i-len(P)+1)
                j = table[j]
            else:
                j += 1
    return result_idx


def solution(T, P):
    KMP(T, P)


def main():
    stdin = sys.stdin
    # 왼쪽 strip 할 경우 index가 달라지므로, rstrip을 해주어야 한다.
    T = stdin.readline().rstrip('\n')
    P = stdin.readline().rstrip('\n')
    result = KMP(T, P)
    print(len(result))
    print(' '.join(str(idx+1) for idx in result))


if __name__ == "__main__":
    main()
    # print(make_table('abacaaba'))
