from typing import List
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnt = Counter([word.lower() for word in re.split(r"[^\w]+", paragraph) if word])
        for banned_word in banned:
            del cnt[banned_word]
        return cnt.most_common()[0][0]


class Solution2:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        return Counter(words).most_common()[0][0]


paragraph = "..Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))
print(Solution2().mostCommonWord(paragraph, banned))
