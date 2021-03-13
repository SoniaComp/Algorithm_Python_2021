from itertools import combinations

def solution(orders, course):
    answer = []
    for course_num in course:
        orders_list = list(filter(lambda x: len(x) >= course_num, orders))
        courses_checked = {}
        for idx in range(len(orders_list)):
            order = orders_list[idx]
            course_candidates = list(combinations(order, course_num))
            for course_candidate in course_candidates:
                candidate_key = ''.join(sorted(list(course_candidate)))
                if not (candidate_key in courses_checked):
                    count = 1
                    for i in range(idx+1, len(orders_list)):
                        if not (set(course_candidate) - set(orders_list[i])):
                            count += 1
                    if count >= 2:
                        courses_checked[candidate_key] = count
        sorted_courses_checked = sorted(courses_checked.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_courses_checked):
            max = sorted_courses_checked[0][1]
            for c in sorted_courses_checked:
                if c[1] == max:
                    answer.append(c[0])
                else:
                    break
    answer.sort()
    return answer