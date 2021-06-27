S1 = "{[()()]}"
S2 = "([)()]"


def solution(S):
    # write your code in Python 3.6
    st = []
    for i in S:
        if i in ['{', '(', '[']:
            st.append(i)
        else:
            # }, ), ] 가 먼저 나오면 stack에 길이가 0이므로 0 리턴
            if len(st) == 0:
                return 0

            if i == '}':
                if st.pop() != '{':
                    return 0
            if i == ')':
                if st.pop() != '(':
                    return 0
            if i == ']':
                if st.pop() != '[':
                    return 0
    # {, (, [ 의 갯수가 더많을경우 stack에 1개이상 쌓여있으므로
    if len(st) > 0:
        return 0

    return 1


print(solution(S1))
print(solution(S2))

#출처 : https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/