def merge_sort(list):
    if len(list) <= 1:
        return list
    
    # 분할
    mid = len(list)//2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    
    # 정복
    return merge(leftList, rightList)
    
    # 1 4 6 5 <- [1, 4, 5, 6]
    # 1 4 / 6 5 <- [1, 4] / [ 5, 6]
    # 1 / 4 / 6 / 5
    
def merge(left, right):
    result = []
    
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.extend(left)
            left = []
        elif len(right) > 0:
            result.extend(right)
            right = []
            
    return result