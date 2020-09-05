import sys

solution1=[[0], [0, 0, 0, 0]]
solution2=[[0, 0]]
solution3=[[0, 0, 1], [1, 0]]
solution4=[[1, 0, 0], [0, 1]]
solution5=[[0, 0, 0], [1, 0], [1, 0, 1], [0, 1]]
solution6=[[0, 0, 0], [2, 0], [0, 1, 1], [0, 0]]
solution7=[[0, 0, 0], [0, 0], [1, 1, 0], [0, 2]]
match = {1: solution1, 2: solution2, 3:solution3, 4:solution4, 5:solution5, 6:solution6, 7:solution7}

def solution(C, P):
    answer = 0
    
    field = list(map(int, input().split()))
    blocks = match[P]
    for block in blocks:
        for i in range(C-len(block)+1):
            if len(block)==1:
                answer+=1
                continue
            for j in range(len(block)-1):
                if block[j]-field[i+j] != block[j+1]-field[i+j+1]:
                    break
                if j == len(block)-2:
                    answer += 1
                    
    print(answer)
    return answer

C, P = map(int, input().split())
solution(C, P)