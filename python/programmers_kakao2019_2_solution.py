from operator import itemgetter

# 일단 따라 쳐봤다.

def iter_gaps_with_indices(xs):
  idx_with_xs = sorted(enumerate(xs), key=itemgetter(1))
  # O(NlogN) # ex) [(1, 1), (2, 2), (0, 3)]
  yield idx_with_xs[0]
  for (_, pt), (idx, t) in zip(idx_with_xs, idx_with_xs[1:]):
    yield idx, t - pt

def solution(food_times, k):
  remain_time = k
  remain_food_count = len(food_times)
  remain_foods = [True]*len(food_times) # O(N)
  gaps_with_indices = iter_gaps_with_indices(food_times) # O(NlogN)
  for idx, food_time in gaps_with_indices: # O(N)
    if food_time * remain_food_count > remain_time:
      break
    remain_time -= food_time * remain_food_count
    remain_food_count -= 1
    remain_foods[idx] = False

  else:
    return -1
  
  nth = remain_time % remain_food_count
  compact_indices = [idx for idx, remained in enumerate(remain_foods) if remained]
  result = compact_indices[nth]
  return result + 1

# 우선 모르는 문법부터 정리해볼까
'''
1. yield(https://dojang.io/mod/page/view.php?id=2412)
yield를 사용하여 바깥으로 전달한 값은 next 함수(__next__ 메서드)의 반환값으로 나온다고 했습니다. 

2. enumerate(https://wikidocs.net/16045)
반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.

3. itemgetter(https://docs.python.org/ko/3.7/library/operator.html#operator.itemgetter)
피연산자의 __getitem__() 메서드를 사용하여 피연산자에서 item을 꺼내는 콜러블 객체를 반환합니다. 여러 항목이 지정되면, 조회 값의 튜플을 반환합니다.

4. zip(https://wikidocs.net/32#zip)
zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.

'''

# 이 문제에 대한 해설도 궁금하다