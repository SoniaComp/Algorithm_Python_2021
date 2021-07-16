num_str = {
    '1': '일',
    '2': '이',
    '3': '삼',
    '4': '사',
    '5': '오',
    '6': '육',
    '7': '칠',
    '8': '팔',
    '9': '구',
    '0': '영'
}


def solution2(num):
    result = ''

    num_reversed = list(str(num))
    num_reversed.reverse()
    N_LEN = len(num_reversed)

    if N_LEN == 1:
        return num_str[num]

    maj_units = ['만', '억', '조', '경', '해', '자', '양', '구', '간', '정', '재', '극']
    units = ['']  # 맨 마지막 일의 자리수는 단위가 붙지 않음

    for maj_unit in maj_units:
        units.extend(['십', '백', '천'])
        units.append(maj_unit)

    for i in range(N_LEN):
        str_num = num_str[num_reversed[i]]
        # 모두 0000 일때는 생략
        if N_LEN >= 9 and i >= 4 and i % 4 == 0 and ''.join(num_reversed[i:i+4]) == '0000':
            continue
        if str_num == '영':
            if i % 4 == 0:
                result = units[i] + result  # 0일때 단위만 붙인다
        else:
            result = str_num + units[i] + result
    return result

# solution2(7342308123)
# >> '칠십삼억사천이백삼십만팔천일백이십삼'