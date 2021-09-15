def solution(A):
    dictionary = {}

    for item in A:
        if item not in dictionary:
            dictionary[item] = 1

    for i in range(1, len(A)+1):
        if i not in dictionary:
            return i

    return len(A) + 1
