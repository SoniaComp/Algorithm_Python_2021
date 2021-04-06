import itertools as it
def substrCount(n, s):
  if n==1: # edge case
    return 1
  s = [list(g) for k, g in it.groupby(s)]
  print(s)
  res = sum([int(len(i)*(len(i)+1)/2) for i in s])
  print(res)

  for i in range(len(s)):
    if i==0 or i==len(s)-1 or len(s[i])>1:
      continue
    if s[i-1][0] == s[i+1][0]:
      res += min(len(s[i-1]), len(s[i+1]))
  return res
