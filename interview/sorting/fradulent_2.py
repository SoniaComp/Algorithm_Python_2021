def get_double_median(counter, d):
    count = 0
    for i in range(201):
        count += counter[i]
        if count > d//2:
            break
    if d % 2 == 1:
        return 2 * i
    else:
        for left in range(i, -1, -1):
            count -= counter[left]
            if count < d//2:
                return left + i
        return 2 * i


def activityNotifications(expenditure, d):
    count = 0
    counter = [0]*201
    for exp in expenditure[:d]:
        counter[exp] += 1
    for i in range(d, len(expenditure)):
        new = expenditure[i]
        old = expenditure[i-d]
        double_median = get_double_median(counter, d)
        if new >= double_median:
            count += 1
        if new == old:
            continue
        counter[new] += 1
        counter[old] -= 1
    return count