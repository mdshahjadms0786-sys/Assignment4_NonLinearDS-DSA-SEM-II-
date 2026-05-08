# Binary Search Tree basic operations
# Insert, Search, Inorder Traversal

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

if __name__ == "__main__":
    keys = [50, 30, 70, 20, 40, 60, 80]
    root = None
    for k in keys:
        root = insert(root, k)

    print("Inorder Traversal (sorted):")
    inorder(root)
    print("\nSearch 40:", "Found" if search(root, 40) else "Not Found")



# Inorder Traversal (sorted):
# 20 30 40 50 60 70 80 
# Search 40: Found
