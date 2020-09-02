import sys


def cal_hash(txt, length):
    val = 0
    for i in range(length):
        val += 2**i * ord(txt[i])
    return val

@profile
def find_txt_hash(txt, idx, length, txt_hash):
    if idx == 0:
        txt_hash.append(cal_hash(txt, length))
    else:
        txt_hash.append((txt_hash[idx-1] - ord(txt[idx-1])) // 2 + (2**(length-1))*ord(txt[idx]))
    return txt_hash


def solution(txt, subtxt):
    subtxt_hash = cal_hash(subtxt, len(subtxt))

    txt_hash = []
    for i in range(len(txt)-len(subtxt)-1):
        txt_hash = find_txt_hash(txt, i, len(subtxt), txt_hash)
        if txt_hash[i] == subtxt_hash:
            return 1

    return 0


def main():
    stdin = sys.stdin
    txt = stdin.readline().strip()
    subtxt = stdin.readline().strip()
    print(solution(txt, subtxt))


if __name__ == '__main__':
    main()

# 이것도 시간초과