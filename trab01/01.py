def char_count(s:str)->int:
    if s:
        return char_count(s[:-1]) + 1
    return 0

def main():
    s = input()
    print('número de caracteres na string de entrada:', char_count(s))

main()
