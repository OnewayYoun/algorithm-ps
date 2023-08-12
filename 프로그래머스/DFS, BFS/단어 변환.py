from collections import deque


def bfs(begin, target, words):
    dq = deque([(begin, 0)])
    visited = [False] * len(words)
    while dq:
        word, cnt = dq.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            if not visited[i]:
                diff_cnt = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff_cnt += 1
                if diff_cnt == 1:
                    dq.append((words[i], cnt + 1))
                    visited[i] = True


def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, target, words)


if __name__ == '__main__':
    begin, target, words = 'hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]  # 4
    # begin, target, words = 'hit', 'cog', ["hot", "dot", "dog", "lot", "log"]  # 0
    print(solution(begin, target, words))
