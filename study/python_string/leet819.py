import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        counts = collections.Counter(words)
        print(counts) # Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
        print(counts.most_common(1)) # [('ball', 2)]

        # 가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
        return counts.most_common(1)[0][0]