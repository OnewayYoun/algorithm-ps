if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'#{i + 1}')
        N = int(input())
        graph = [[None] * N for _ in range(N)]
        curr_x, curr_y = 0, 0
        curr_val = 1
        direction = 'N'
        while curr_val <= N ** 2:
            graph[curr_y][curr_x] = curr_val
            if direction == 'N':
                if 0 <= curr_y - 1 and graph[curr_y - 1][curr_x] is None:
                    curr_y -= 1
                else:
                    direction = 'E'
                    curr_x += 1
            elif direction == 'E':
                if N > curr_x + 1 and graph[curr_y][curr_x + 1] is None:
                    curr_x += 1
                else:
                    direction = 'S'
                    curr_y += 1
            elif direction == 'S':
                if N > curr_y + 1 and graph[curr_y + 1][curr_x] is None:
                    curr_y += 1
                else:
                    direction = 'W'
                    curr_x -= 1
            elif direction == 'W':
                if 0 <= curr_x - 1 and graph[curr_y][curr_x - 1] is None:
                    curr_x -= 1
                else:
                    direction = 'N'
                    curr_y -= 1
            curr_val += 1

        for i in graph:
            print(*i, sep=' ')
