from hashtable import HashTable

def main():
    size = int(input())
    table = HashTable(size)
    while True:
        command = int(input())
        if command != 0 and command != 1:
            break
        text = input()
        if command == 0:
            table.insert(text)
        else:
            table.remove(text)
    print(table)

if __name__ == '__main__':
    main()