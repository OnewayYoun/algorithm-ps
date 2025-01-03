from collections import defaultdict
from typing import List


class Solution:
    """
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Input: strs = [""]
    Output: [[""]]

    Input: strs = ["a"]
    Output: [["a"]]
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for word in strs:
            dd[''.join(sorted(word))].append(word)
        return [val for val in dd.values()]


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
