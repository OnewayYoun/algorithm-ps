import math
from typing import List
import operator


class Solution:
    """
    Input: tokens = ["2","1","+","3","*"]
    Output: 9

    Input: tokens = ["4","13","5","/","+"]
    Output: 6

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    """

    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: math.trunc(a / b),
        }
        stack = []
        for idx, token in enumerate(tokens):
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
        return stack[0]


print(Solution().evalRPN(["4", "-2", "/", "2", "-3", "-", "-"]))
