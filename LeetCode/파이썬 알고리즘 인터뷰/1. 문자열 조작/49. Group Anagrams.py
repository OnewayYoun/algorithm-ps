from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            groups[''.join(sorted(word))].append(word)
        return list(groups.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
