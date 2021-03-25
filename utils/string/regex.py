import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + \
        "".join([st[-1] for i in range(3-len(st))])
    return st

# 문자열 뒤집기
s = 'abc'
s[::-1] == s.revers()

# 문자열 비교 sorted, cmp_to_key
# 두개의 key가 있다면 lambda식 리턴 2개

# key
# extend, sort(), reverse()는 리턴이 아니라 리스트 값 자체를 바꾸는 것
