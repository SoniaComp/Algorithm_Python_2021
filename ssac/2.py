num_str = {
    1: '일',
    2: '이',
    3: '삼',
    4: '사',
    5: '오',
    6: '육',
    7: '칠',
    8: '팔',
    9: '구',
    0: '영'
}


def solution2(num):
    result = ''

    num_reversed = list(str(num))
    num_reversed.reverse()
    N_LEN = len(num_reversed)

    if N_LEN == 1:
        return num_str[num]

    maj_units = ['', '만', '억', '조', '경', '해',
                 '자', '양', '구', '간', '정', '재', '극']

    # 천의 단위로 끊음
    num_units = []
    while num_reversed:
        num_units.append(num_reversed[0:4])
        num_reversed = num_reversed[4:]

    def num_to_str(num_arr, idx):
        result = ''

        if idx >= 1 and ''.join(num_arr) == '0000':
            return result

        min_units = ['', '십', '백', '천']
        for i, num in enumerate(num_arr):
            str_num = num_str[int(num)]
            if str_num == '영':
                continue
            else:
                result = str_num + min_units[i] + result
        return result

    for idx, num_unit in enumerate(num_units):
        result = num_to_str(num_unit, idx) + maj_units[idx] + result

    return result

# solution2(7342308123)
# 칠십삼억사천이백삼십만팔천일백이십삼