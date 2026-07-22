import re


class Solution:
    """
    Input: path = "/home/"
    Output: "/home"

    Input: path = "/home//foo/"
    Output: "/home/foo"

    Input: path = "/home/user/Documents/../Pictures"
    Output: "/home/user/Pictures"

    Input: path = "/../"
    Output: "/"

    Input: path = "/.../a/../b/c/../d/./"
    Output: "/.../b/d"
    """

    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in re.split(r'/', path):
            if i in ('', '.'):
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return '/' + '/'.join(stack)
























    def simplifyPath1(self, path: str) -> str:
        stack = []
        for i in path.split('/'):
            if not i or i == '.':
                continue
            if i == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(i)

        return '/' + '/'.join(stack)

print(Solution().simplifyPath1(path="/.../a/../b/c/../d/./"))
# print(Solution().simplifyPath1(path="/../"))
# Output: "/.../b/d"
