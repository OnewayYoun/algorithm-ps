from collections import deque

parentheses = {'(': ')', '[': ']', '{': '}'}


def solution(s):
    def is_valid(input_str):
        stack = []
        for i in input_str:
            if i in parentheses:
                stack.append(i)
            else:
                if not stack:
                    return False
                if parentheses[stack.pop()] != i:
                    return False
        return True if not stack else False

    dq = deque(s)
    answer = 0
    for _ in range(len(s)):
        dq.rotate(-1)
        if is_valid(''.join(dq)):
            answer += 1
    return answer


'''
def isValid(self, s: str) -> bool:
        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0
'''