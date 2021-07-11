# 2진수로 바꾸기 bin() 그리고 0b가 붙음..
def solution(N):
  current_gap = 0
  max_gap = 0

  start_counting = False

  temp = N

  while temp > 0:
    
    # case1
    if temp & 1 == 1:
      # case 1-1
      if start_counting == False:
        start_counting = True
      # case 1-2
      elif start_counting == True:
        max_gap = max(max_gap, current_gap)
        current_gap = 0

    # case 2
    elif temp & 1 == 0:
      if start_counting == True:
        current_gap += 1
      
    temp = temp >> 1

    return max_gap
    
# 참고: https://github.com/Mickey0521/Codility-Python