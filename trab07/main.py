from typing import List


def get_genomic_distance(lst: List[int]):
    distance = 0

    fake_lst = lst.copy()
    n = len(lst)
    for i in range(n):
        lst[i] = lst[i]
        for j in range(i+1, n):
            if lst[j] < lst[i]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
                distance += 1

    return distance


def main():
    size = int(input())
    lst = [int(w) for w in input().split()]
    genomic_distance = get_genomic_distance(lst)
    print(genomic_distance)


if __name__ == '__main__':
    main()