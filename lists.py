class Node:
    def __init__(self, value):
        self.back = None
        self.next = None
        self.value = str(value)

def adds(node, value):
    current = node
    while current.next is not None:
        current = current.next

    new_node = Node(value)
    new_node.back = current
    current.next = new_node

def lists(node):
    current = node
    while current is not None:
        print(current.value)
        current = current.next

# criar lista
root = Node("root")

for a in range(10):
    adds(root, "node " + str(a))

lists(root)