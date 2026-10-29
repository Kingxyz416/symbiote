
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.child = []

    def display(self):
        print(self.keys)
        for c in self.child:
            c.display()


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True

        if node.leaf:
            return False

        return self.search(node.child[i], key)

    def insert(self, key):
        root = self.root

        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t)
            new_root.child.append(root)
            self.split(new_root, 0)
            self.root = new_root

        self.insert_key(self.root, key)

    def insert_key(self, node, key):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key

        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            if len(node.child[i].keys) == 2 * self.t - 1:
                self.split(node, i)
                if key > node.keys[i]:
                    i += 1

            self.insert_key(node.child[i], key)

    def split(self, node, i):
        t = self.t
        old_child = node.child[i]
        new_child = BTreeNode(t, old_child.leaf)

        middle = old_child.keys[t - 1]
        new_child.keys = old_child.keys[t:]
        old_child.keys = old_child.keys[:t - 1]

        if not old_child.leaf:
            new_child.child = old_child.child[t:]
            old_child.child = old_child.child[:t]

        node.child.insert(i + 1, new_child)
        node.keys.insert(i, middle)


# Main program
t = int(input("Enter minimum degree of B-Tree: "))
tree = BTree(t)

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        key = int(input("Enter value to insert: "))
        tree.insert(key)
        print("Value inserted successfully")

    elif ch == 2:
        key = int(input("Enter value to search: "))
        if tree.search(tree.root, key):
            print("Value found")
        else:
            print("Value not found")

    elif ch == 3:
        print("B-Tree:")
        tree.root.display()

    elif ch == 4:
        break

    else:
        print("Invalid choice")
