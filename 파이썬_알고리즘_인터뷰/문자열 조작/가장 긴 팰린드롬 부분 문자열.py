def longest_palindrome(s: str):
    if len(s) <= 1 or s == s[::-1]:
        return s

    def expand(left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    res = ''
    for i in range(len(s) - 1):
        res = max(res, expand(i, i), expand(i, i + 1), key=len)
    return res


print(longest_palindrome("abcccb"))
