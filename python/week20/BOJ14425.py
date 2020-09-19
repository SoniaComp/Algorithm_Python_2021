# 이건 트라이가 좋을 듯
import sys


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        return True

# def solution(N, M):
#     trie = Trie()
#     stdin = sys.stdin
#     for i in range(N):
#         trie.insert(str(stdin.readline().strip()))
#     ans = 0
#     for j in range(M):
#         if trie.search(str(stdin.readline().strip())):
#           ans+=1
#     return ans

def solution(N, M):
  input = sys.stdin.readline
  strings = [input().rtrip() for _ in range(N)]
  ans = 0

  for i in range(M):
    string = input().rstrip()
    if string in strings:
      ans += 1

  return ans


def main():
    stdin = sys.stdin
    N, M = map(int, input().split())
    print(solution(N, M))


if __name__ == "__main__":
    main()
