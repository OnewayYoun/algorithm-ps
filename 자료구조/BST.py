class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node


def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)


# Driver Code
if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print(search(root, 30))
    print(search(root, 100))


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, head):
        self.head = head

    def insert_node(self, value):
        self.base_node = self.head
        while True:
            if self.base_node.value > value:
                if self.base_node.left is not None:
                    self.base_node = self.base_node.left
                else:
                    self.base_node.left = Node(value)
                    break
            else:
                if self.base_node.right is not None:
                    self.base_node = self.base_node.right
                else:
                    self.base_node.right = Node(value)
                    break

    def search_node(self, value):
        self.base_node = self.head
        while self.base_node:
            if self.base_node.value == value:
                return True
            elif self.base_node.value > value:
                if self.base_node.left is not None:
                    self.base_node = self.base_node.left
                else:
                    return False
            elif self.base_node.value < value:
                if self.base_node.right is not None:
                    self.base_node = self.base_node.right
                else:
                    return False


head = Node(50)
bt = BinarySearchTree(head)
bt.insert_node(30)
bt.insert_node(20)
bt.insert_node(40)
bt.insert_node(70)
bt.insert_node(60)
bt.insert_node(80)

print(bt.search_node(30))
print(bt.search_node(15))
