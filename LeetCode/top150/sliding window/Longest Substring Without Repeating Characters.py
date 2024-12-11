class Solution:
    """
    Input: s = "abcabcbb"
    Output: 3

    Input: s = "bbbbb"
    Output: 1

    Input: s = "pwwkew"
    Output: 3
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        store = set()

        for right in range(len(s)):
            if s[right] not in store:
                store.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[left] != s[right]:
                    store.remove(s[left])
                    left += 1
                left += 1
        return max_length


print(Solution().lengthOfLongestSubstring("abbbaea"))
# print(Solution().lengthOfLongestSubstring("abcabcbb"))
