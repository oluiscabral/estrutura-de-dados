def is_ascending(lst)->bool:
    if len(lst) < 2:
        return True
    if lst[0] >= lst[1]:
        return False
    return is_ascending(lst[1:])

def main():
    lst = [int(w) for w in input().split()]
    print(is_ascending(lst))

main()
