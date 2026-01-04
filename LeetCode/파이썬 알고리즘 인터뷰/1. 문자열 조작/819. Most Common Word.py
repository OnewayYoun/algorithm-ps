from typing import List
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_paragraph = re.sub(r"[^a-zA-Z ]", " ", paragraph)
        print(new_paragraph.split(" "))
        counter = Counter(new_paragraph.lower().split()).most_common()
        answer_idx = 0
        for i in range(len(banned)):
            if counter[i][0] not in banned:
                return counter[i][0]
            answer_idx += 1
        return counter[answer_idx][0]


if __name__ == "__main__":
    print(Solution().mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]))
