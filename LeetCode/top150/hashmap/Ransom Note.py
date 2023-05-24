from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = Counter(ransomNote), Counter(magazine)
        if r & m == r:
            return True
        return False


if __name__ == '__main__':
    ransomNote = "aac"
    magazine = "aaaaccc"
    output = True

    print(output == Solution().canConstruct(ransomNote, magazine))
