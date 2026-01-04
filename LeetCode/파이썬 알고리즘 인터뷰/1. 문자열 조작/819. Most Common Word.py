from typing import List
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_paragraph = re.sub(r"[^a-zA-Z]", " ", paragraph)
        counter = Counter([word for word in new_paragraph.lower().split() if word not in banned])
        return counter.most_common(1)[0][0]


if __name__ == "__main__":
    print(Solution().mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]))
