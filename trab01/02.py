def print_reversed(s:str):
    if s:
        print(s[-1])
        print_reversed(s[:-1])

def main():
    s = input()
    print_reversed(s)

main()
