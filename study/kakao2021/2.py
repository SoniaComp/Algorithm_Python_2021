from itertools import combinations
from collections import Counter


def solution(orders, course):
    #     answer = []
    result = []
#     for course_num in course:
    for course_size in course:
        order_combinations = []
#         orders_list = list(filter(lambda x: len(x) >= course_num, orders))
#         courses_checked = {}
#         for idx in range(len(orders_list)):
#             order = orders_list[idx]
#             course_candidates = list(combinations(order, course_num))
#             for course_candidate in course_candidates:
#                 candidate_key = ''.join(sorted(list(course_candidate)))
#                 if not (candidate_key in courses_checked):
#                     count = 1
#                     for i in range(idx+1, len(orders_list)):
#                         if not (set(course_candidate) - set(orders_list[i])):
#                             count += 1
#                     if count >= 2:
#                         courses_checked[candidate_key] = count
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)
#         sorted_courses_checked = sorted(courses_checked.items(), key=lambda x: x[1], reverse=True)
#         if len(sorted_courses_checked):
#             max = sorted_courses_checked[0][1]
#             for c in sorted_courses_checked:
#                 if c[1] == max:
#                     answer.append(c[0])
#                 else:
#                     break
        most_ordered = Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v >
                   1 and v == most_ordered[0][1]]
#     answer.sort()
#     return answer
    return [''.join(v) for v in sorted(result)]
    # 마지막에 처리해주기

# class collections.Counter([iterable-or-mapping])¶
# Counter는 해시 가능한 객체를 세기 위한 dict 서브 클래스입니다. 요소가 딕셔너리 키로 저장되고 개수가 딕셔너리값으로 저장되는 컬렉션입니다. 개수는 0이나 음수를 포함하는 임의의 정숫값이 될 수 있습니다. Counter 클래스는 다른 언어의 백(bag)이나 멀티 셋(multiset)과 유사합니다.

# collections Counter
# -> 0으로 초기화하지 않아도 된다는 장점을 가지고 있다.

# https://www.daleseo.com/python-collections-counter/
# https://wikidocs.net/84392 collections의 다른 함수
# Counter 클래스는 파이썬의 기본 자료구조인 사전(dictionary)를 확장하고 있기 때문에, 사전에서 제공하는 API를 그대로 다 사용할 수가 있습니다.
# 카운팅을 더 잘할 수 있도록, 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 most_common이라는 메서드를 제공하고 있습니다.
