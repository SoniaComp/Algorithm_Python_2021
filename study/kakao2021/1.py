import re

def trim_dot(string):
    if string == '.' or string == '':
        return ''
    if string[0] == '.':
        string = string[1:]
    if string[-1] == '.':
        string = string[:-1]
    return string

def solution(new_id):
    answer = new_id
    # 1
    if not answer.islower():
        answer = answer.lower()
    # 2
    answer = re.sub('[^a-z0-9-_\.]', '', answer)
    # 3
    answer = re.sub('\.{2,}', '.', answer)
    # 4
    answer = trim_dot(answer)
    # 5,6
    id_length = len(answer)
    if id_length == 0:
        answer = 'a'
    elif id_length >= 16:
        answer = answer[:15]
        answer = trim_dot(answer)
    # 7
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))    
    return answer