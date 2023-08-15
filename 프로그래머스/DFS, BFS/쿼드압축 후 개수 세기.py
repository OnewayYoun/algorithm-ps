def solution(graph):
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

    answer = []
    traverse_quad_tree(0, 0, len(graph))
    return [answer.count(0), answer.count(1)]


if __name__ == '__main__':
    graph = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
    print(solution(graph))
