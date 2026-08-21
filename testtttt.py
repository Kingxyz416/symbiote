class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

root = None
for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

key = int(input("Enter key to search: "))

if search(root, key):
    print("Key found in BST")
else:
    print("Key not found in BST")
