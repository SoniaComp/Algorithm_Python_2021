def solution1(X, A):
    leafs = [(num, i) for i, num in enumerate(A)]
    leafs = sorted(leafs)
    cur_num = 0
    max_num = 0
    for leaf in leafs:
        num, i = leaf[0], leaf[1]
        if num - cur_num > 1:
            return -1
        if num - cur_num == 0:
            continue
        elif num - cur_num == 1:
            max_num = max(max_num, i)
            cur_num = num
        if num == X:
            return max_num
    return -1

def solution2(A):
  if max(A) != len(A) or len(set(A)) != len(A):
    return 0
  return 1

def solution3(A):
  N = len(A)

  xorSum = 0
  for i in range(1, N+1):
    xorSum ^= i ^ A[i-1]

  if xorSum == 0:
    return 1
  else:
    return 0