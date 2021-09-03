from balancedtree import BalancedTree


def main():
    tree = BalancedTree()
    n = int(input())
    for _ in range(n):
        value = int(input())
        tree.insert(value)
    print(*tree.preordered(), sep=" ")
    print(*tree.ordered(), sep=" ")
    print(*tree.postordered(), sep=" ")


if __name__ == '__main__':
    main()
