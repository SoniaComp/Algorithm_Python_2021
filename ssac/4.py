def solution4(n, k):
    count = 0
    for num in range(n+1):
        count += list(str(num)).count(str(k))
    return count

# solution4(343356, 9)
# >> 166965