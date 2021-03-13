def solution(infos, querys):
    answer = []

    # info 데이터 전처리
    for i in range(len(infos)):
        info = infos[i]
        info = info.split(' ')
        info = list(map(lambda x: x if x.isnumeric() else x[0], info))
        infos[i] = ''.join(info)

    # query 데이터 전처리
    for i in range(len(querys)):
        query = querys[i]
        query = query.replace(' and', '').split(' ')
        query = list(map(lambda x: x if x.isnumeric() else x[0], query))
        querys[i] = ''.join(query)

    for query in querys:
        match_count = 0
        for info in infos:
            query_str = ''.join(
                list(map(lambda x: info[x[0]] if x[1] == '-' else x[1], enumerate(query[:4]))))
            if query_str == info[:4] and int(info[4:]) >= int(query[4:]):
                match_count += 1
        answer.append(match_count)

    return answer
