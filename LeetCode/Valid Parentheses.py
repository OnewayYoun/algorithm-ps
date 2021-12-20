class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i in ['(', '[', '{']:
                st.append(i)
            else:
                if not st:
                    return False
                if i == ')':
                    if st.pop() != '(':
                        return False
                elif i == ']':
                    if st.pop() != '[':
                        return False
                else:
                    if st.pop() != '{':
                        return False
        if st:
            return False
        else:
            return True


if __name__ == '__main__':
    s = "([()[]]{})"
    S = Solution()
    print(S.isValid(s))
