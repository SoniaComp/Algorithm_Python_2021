# 반드시 다른 풀이를 살펴보는 것을 추천한다.
# 다른 사람의 논리를 보면서, 항상 배움이 있다!!
import os

# Complete the isValid function below.
A_ASCII = ord('a')
def isValid(s): 
    ret = 'YES'
    scount = [0 for i in range(26)]
    for i in s:
      scount[ord[i]-A_ASCII] += 1
    # 결과 값
    aux = [i for i in scount if i!=0]
    d = {}
    max_value = 0
    for i in aux:
      d[i] = d.get(i, 0) + 1
      if d[i] > max_value:
        max_key, max_value = i, d[i] # most_frequent
    diff_elem_count = 0

    for i in d:
      if i != max_key:
        if i == max_key+1 or i == 1:
          diff_elem_count += d[i]
          if diff_elem_count > 1:
            ret = 'NO'
            break
        else:
          ret= 'NO'
          break
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()