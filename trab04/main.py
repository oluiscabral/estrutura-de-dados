from binarytree import BinaryTree

def main(n):
    tree = BinaryTree()
    for i in range(n):
        tree.append(int(input()))
    root = tree[0]
    preordered = tree.preorder(root)
    ordered = tree.order(root)
    postordered = tree.postorder(root)
    print(*preordered, sep=" ")
    print(*ordered, sep=" ")
    print(*postordered, sep=" ")

if __name__ == "__main__":
    n = int(input())
    main(n)