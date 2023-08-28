# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def __str__(self):
#         return ' -> '.join(map(str, self.queue))
#
#     def __len__(self):
#         return len(self.queue)
#
#     def push(self, data):
#         self.queue.append(data)
#
#     def popleft(self):
#         return self.queue.pop(0)


class Queue:
    def __init__(self):
        self.st_in = []
        self.st_out = []

    def push(self, data):
        self.st_in.append(data)

    def transfer(self):
        while self.st_in:
            self.st_out.append(self.st_in.pop())

    def popleft(self):
        if not self.st_out:
            self.transfer()
        return self.st_out.pop()

    def __str__(self):
        return ''.join(map(str, self.st_out[::-1])) + ''.join(map(str, self.st_in))


q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q)
q.popleft()
q.push(4)
print(q)


# print(q.popleft())
# print(q.popleft())
# print(q.popleft())
