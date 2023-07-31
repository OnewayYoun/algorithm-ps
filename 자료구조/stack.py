class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return ' -> '.join(map(str, self.stack))

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()


st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st, len(st), sep='\n')
print(st.pop() == 4)
print(st, len(st), sep='\n')
