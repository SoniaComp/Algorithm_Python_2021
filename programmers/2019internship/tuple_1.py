def solution(s):
    sets = [set()]
    result = []
    elements = s.rstrip('}').lstrip('{').split('},{')
    for element in elements:
        sets.append(set(element.split(',')))
    sets.sort(key=len)
    for i in range(len(sets)):
        result.append(sets[i] - sets[i-1])
    return list(map(lambda x: int(list(x)[0]), sets[1:]))