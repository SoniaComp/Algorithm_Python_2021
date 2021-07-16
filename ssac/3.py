def solution3(k, w, capitals, profits):
    PROJ_LEN = len(capitals)
    projects = list()
    
    for i in range(PROJ_LEN):
        projects.append((capitals[i], profits[i]))
        
    sum_w = w
    for i in range(k):
        possible_projects = sorted(list(filter(lambda x:x[0] <= sum_w, projects)), key=lambda x:x[1])
        proj = possible_projects.pop()
        sum_w += proj[1]
    return sum_w

# solution3(3, 0, [0, 2, 4, 3, 0], [1, 3, 5, 1, 2])
# >> 10