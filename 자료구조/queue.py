class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' -> '.join(map(str, self.queue))

    def __len__(self):
        return len(self.queue)

    def push(self, data):
        self.queue.append(data)

    def popleft(self):
        return self.queue.pop(0)


q = Queue()
q.push(1)
q.push(2)
q.push(3)

print(q, len(q), sep='\n')
print(q.popleft() == 1)
print(q, len(q), sep='\n')
