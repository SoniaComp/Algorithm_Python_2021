# 내가 좋아하는 풀이
# https://stackoverflow.com/questions/48951591/python-find-longest-binary-gap-in-binary-representation-of-an-integer-number

def solution(N):
  xs = bin(N)[2:].strip('0').split('1')
  return max([len(x) for x in xs])

def solution2(N):
  return len(max(format(N, 'b').strip('0').split('1')))