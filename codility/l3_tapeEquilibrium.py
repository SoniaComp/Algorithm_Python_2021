def solution(A):
  sum_of_part_one = 0
  sum_of_part_two = sum(A)
  min_difference = None

  for i in range(1, len(A)):
    sum_of_part_one += A[i-1]
    sum_of_part_two -= A[i-1]
    difference = abs(sum_of_part_one - sum_of_part_two)

    if min_difference == None:
      min_difference = difference
    else:
      min_difference = min(min_difference, difference)
  
  return min_difference