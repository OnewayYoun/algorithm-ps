from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for word in strs:
            dd[''.join(sorted(word))].append(word)
        return list(dd.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
