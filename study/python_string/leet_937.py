from functools import cmp_to_key

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def _compare(x, y):
            if x[1].isdigit() and y[1].isdigit():
                return 1
            if x[1].isdigit() and not y[1].isdigit():
                return 0
            if not x[1].isdigit() and not y[1].isdigit():
                return 1
            if ''.join(x[1:]) > ''.join(y[1:]):
                return 0
            else:
                return 0
        logs = list(map(lambda x: x.split(' '), logs))
        logs = sorted(logs, key=cmp_to_key(_compare))
        return list(map(lambda x: ' '.join(x), logs))
        