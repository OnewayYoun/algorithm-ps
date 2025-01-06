from typing import List


class Solution:
    """
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def move_left():
            nonlocal cur_x, cur_y, cur_direction
            while 0 <= cur_y < y and not visited[cur_x][cur_y]:
                answer.append(matrix[cur_x][cur_y])
                visited[cur_x][cur_y] = True
                cur_y -= 1
            cur_y += 1
            cur_x -= 1
            cur_direction = 'Up'

        def move_right():
            nonlocal cur_x, cur_y, cur_direction
            while 0 <= cur_y < y and not visited[cur_x][cur_y]:
                answer.append(matrix[cur_x][cur_y])
                visited[cur_x][cur_y] = True
                cur_y += 1
            cur_y -= 1
            cur_x += 1
            cur_direction = 'Down'

        def move_up():
            nonlocal cur_x, cur_y, cur_direction
            while 0 <= cur_x < x and not visited[cur_x][cur_y]:
                answer.append(matrix[cur_x][cur_y])
                visited[cur_x][cur_y] = True
                cur_x -= 1
            cur_x += 1
            cur_y += 1
            cur_direction = 'Right'

        def move_down():
            nonlocal cur_x, cur_y, cur_direction
            while 0 <= cur_x < x and not visited[cur_x][cur_y]:
                answer.append(matrix[cur_x][cur_y])
                visited[cur_x][cur_y] = True
                cur_x += 1
            cur_x -= 1
            cur_y -= 1
            cur_direction = 'Left'

        answer = []
        x, y = len(matrix), len(matrix[0])
        cur_x, cur_y = 0, 0
        visited = [[False] * y for _ in range(x)]
        cur_direction = 'Right'
        while 0 <= cur_x < x and 0 <= cur_y < y and not visited[cur_x][cur_y]:
            if cur_direction == 'Right':
                move_right()
            elif cur_direction == 'Left':
                move_left()
            elif cur_direction == 'Up':
                move_up()
            elif cur_direction == 'Down':
                move_down()

        return answer

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        while matrix:
            answer += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return answer


print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(Solution().spiralOrder2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


# arr = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]]

# list(map(list, zip(*reversed(arr))))  # 90도 회전 (오른쪽으로 90도)
# list(map(lambda x: list(reversed(x)), reversed(arr)))  # 180도 회전
# list(reversed(list(map(list, zip(*arr)))))  # 270도 회전 (왼쪽으로 90도)
