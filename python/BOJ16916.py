import sys


def compare_txt(stack, subtxt):
    flag = True
    for i in range(-1, (-len(subtxt))-1, -1):
        if stack[i] != subtxt[i]:
            flag = False
            break
    return flag


def solution(txt, subtxt):
    stack = []
    for i in range(len(txt)):
      stack.append(txt[i])
      if len(stack) >= len(subtxt):
        if compare_txt(stack, subtxt):
          return 1
    return 0


def main():
    stdin = sys.stdin
    txt = stdin.readline().strip()
    subtxt = stdin.readline().strip()
    print(solution(txt, subtxt))


if __name__ == '__main__':
    main()
