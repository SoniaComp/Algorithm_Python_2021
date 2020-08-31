import sys

@profile
def solution(string, bomb):
    while(1):
        astring = string.split(bomb)
        newstring = ''.join(astring)
        if newstring == string:
            break
        string = newstring

    if string == '':
        return 'FRULA'
    else:
        return string


def main():
    stdin = sys.stdin
    string = stdin.readline().strip()
    bomb = stdin.readline().strip()
    print(solution(string, bomb))


if __name__ == '__main__':
    main()

# 문자열 관련 함수(파이썬): https://wayhome25.github.io/python/2017/02/26/py-14-list/

# find, index
# find: 문자나 문자열이 없을 경우 -1 return
# index: 없을 경우 오류 발생

# strip: getting-rid-of-/n-when-using-readlines