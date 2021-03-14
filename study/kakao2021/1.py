import re

# def trim_dot(string):
#     if string == '.' or string == '':
#         return ''
#     if string[0] == '.':
#         string = string[1:]
#     if string[-1] == '.':
#         string = string[:-1]
#     return string

def solution(new_id):
#     answer = new_id
    st = new_id
#     # 1
#     if not answer.islower():
#         answer = answer.lower()
    st = st.lower()
#     # 2
#     answer = re.sub('[^a-z0-9-_\.]', '', answer)
    st = re.sub('[^a-z0-9\-_.]', '', st)
#     # 3
#     answer = re.sub('\.{2,}', '.', answer)
    st = re.sub('\.+', '.', st)
#     # 4
#     answer = trim_dot(answer)
    st = re.sub('^[.]|[.]$', '', st)
#     # 5,6
#     id_length = len(answer)
#     if id_length == 0:
#         answer = 'a'
#     elif id_length >= 16:
#         answer = answer[:15]
#         answer = trim_dot(answer)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
#     # 7
#     if len(answer) <= 2:
#         answer += answer[-1] * (3 - len(answer))    
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return answer
    return st

# for 대신 inline for문 / range를 사용하고
# if 대신 삼항 연산자를 사용하는 것이
# 더 파이썬 스럽구나를 느꼈다.
# 정규식 튜토리얼의 고수님을 만났당.. 
# https://chrisjune-13837.medium.com/%EC%A0%95%EA%B7%9C%EC%8B%9D-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-%EC%98%88%EC%A0%9C%EB%A5%BC-%ED%86%B5%ED%95%9C-cheatsheet-%EB%B2%88%EC%97%AD-61c3099cdca8