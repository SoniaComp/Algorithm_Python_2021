from itertools import combinations

def solution(relation):
    N = len(relation)
    CN = len(relation[0])
    if CN == 1:
        return 1
    unique = []
    idxs = [i for i in range(CN)]
    # 유일성 검증
    for n in range(1, N+1):
        for r in combinations(idxs, n):
            sets = []
            for row in relation:
                sets.append(''.join([row[i] for i in range(CN) if i in r]))
            sets = set(sets)
            if len(sets) == N:
                unique.append(r)
    answer = []
    unique = list(reversed(unique))
    while unique:
        element = unique.pop()
        answer.append(element)
        del_list = []
        for other_element in unique:
            if set(element).issubset(set(other_element)):
                del_list.append(other_element)
        for del_element in del_list:
            unique.remove(del_element)
    return len(answer)
 