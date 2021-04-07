from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    ans = []
    freqs = defaultdict(int) # {count: [num]}
    count = defaultdict(int) # {num: count}
    for query in queries:
        if query[0] == 1:
            cur_count = count[query[1]]
            count[query[1]] += 1
            freqs[cur_count] -= 1
            freqs[cur_count+1] += 1
        elif query[0] == 2 and count[query[1]]:
            cur_count = count[query[1]]
            count[query[1]] -= 1
            freqs[cur_count] -= 1
            freqs[cur_count-1] += 1
        elif query[0] == 3:
            ans.append(1 if freqs[query[1]] else 0)
    return ans
    