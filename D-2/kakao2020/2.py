def transform(p):
    if not p:
        return p
    
    balance = 0
    for idx, char in enumerate(p):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            u, v = p[:idx+1], p[idx+1:]
            if u[0] == '(': # 올바른 괄호 문자열
                return u + transform(v)
            else:
                return '('+transform(v)+')'+ ''.join(list(map(lambda x: ')' if x == '(' else '(', u[1:-1])))
    
def solution(p):
    return transform(p)