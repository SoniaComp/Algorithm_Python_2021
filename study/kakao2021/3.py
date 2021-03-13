def solution(infos, querys):
    answer = []
    
    # info 데이터 전처리
    for i in range(len(infos)):
        info = infos[i]
        info = info.split(' ')
        info = list(map(lambda x: int(x) if x.isnumeric() else x[0], info))
        infos[i] = info
        
    # query 데이터 전처리
    for i in range(len(querys)):
        query = querys[i]
        query = query.replace(' and', '')
        query = query.split(' ')
        query = list(map(lambda x: int(x) if x.isnumeric() else x[0], query))
        querys[i] = query

    for query in querys:
        match_count = 0
        for info in infos:
            condition_flag = False
            for i in range(4): # 5개 조건
                if query[i] != '-' and query[i] != info[i]:
                    break
                if i == 3:
                    condition_flag = True
            if condition_flag and info[4] >= int(query[4]):
                    match_count += 1
        answer.append(match_count)
    
    return answer