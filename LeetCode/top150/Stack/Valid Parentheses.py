class Solution:
    """
    Input: s = "()"
    Output: true

    Input: s = "()[]{}"
    Output: true

    Input: s = "(]"
    Output: false
    """

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            else:
                if stack:
                    if char == ')' and stack.pop() != '(':
                        return False
                    elif char == '}' and stack.pop() != '{':
                        return False
                    elif char == ']' and stack.pop() != '[':
                        return False
                else:
                    return False
        return True if not stack else False

    def isValid1(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack

    def isValid2(self, s: str) -> bool:
        for _ in range(len(s)//2):
            s = s.replace('{}', '').replace('[]', '').replace('()', '')
        return not s

# print(Solution().isValid("("))
# print(Solution().isValid1("("))
print(Solution().isValid2("(]"))
