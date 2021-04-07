from collections import defaultdict
# Complete the countTriplets function below.
# https://www.snoopybox.co.kr/1794
# DP + HASH
def countTriplets(arr, r):
    total = 0
    small, large = defaultdict(int), defaultdict(int)
    for a in arr:
        large[a] += 1
    for a in arr:
        large[a] -= 1
        if a % r == 0:
            total += large[a*r] * small[a//r]
        small[a] += 1
    return total