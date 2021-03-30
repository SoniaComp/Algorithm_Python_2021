# 연산자 우선순위는 최대 6개까지 나올 수 있습니다.
# 그떄 그때 저장한다.
# 이때, 배열 해놓으면 훨씬 편할 수 있다.

from itertools import permutations
import re

def solution(expression):
  expressions = set(re.findall("\D", expression)) # 숫자가 아닌 것 \D
  prior = permutations(expressions)
  cand = []

  for op_cand in prior:
    calc = re.compile("(\D)").split('' + expression)
    for exp in op_cand:
      while exp in calc:
        idx = calc.index(exp)
        calc = calc[:idx-1] + [str(eval(''.join(calc[idx-1:idx+2])))] + calc[idx+2:]
    cand.append(abs(int(calc[0])))
  return max(cand)
  
