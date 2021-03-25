from functools import cmp_to_key

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        strings = []
        for log in logs:
            log_splits = log.split(' ')
            if log_splits[1].isdigit():
                digits.append(log)
            else:
                strings.append(log_splits)
        def compare(x, y):
            if ''.join(x[1:]) > ''.join(y[1:]):
                return 1
            elif ''.join(x[1:]) == ''.join(y[1:]) and x[0] > y[0]:
                return 1
            else:
                return 0
        strings = sorted(strings, key=cmp_to_key(compare))
        result = list(map(lambda x: ' '.join(x), strings))
        result.extend(digits)
        return result

'''spit() == split(' ')
If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].
'''