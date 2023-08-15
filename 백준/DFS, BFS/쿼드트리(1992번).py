"""
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
"""
import sys

input = sys.stdin.readline


# sys.setrecursionlimit(10 ** 5)


def traverse_quad_tree(x, y, n):
    new_n = n // 2
    for i in range(n):
        for j in range(n):
            if graph[y][x] != graph[y + i][x + j]:
                answer.append('(')
                traverse_quad_tree(x, y, new_n)
                traverse_quad_tree(x + new_n, y, new_n)
                traverse_quad_tree(x, y + new_n, new_n)
                traverse_quad_tree(x + new_n, y + new_n, new_n)
                answer.append(')')
                return
    answer.append(graph[y][x])


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, list(input().strip()))) for _ in range(N)]
    answer = []
    traverse_quad_tree(0, 0, N)
    print(''.join(map(str, answer)))
